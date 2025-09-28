#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <string>
#include <queue>
#include <set>
#include <WinSock2.h>
#include <locale>
#include <codecvt>

#pragma warning(disable : 4996)
#pragma comment(lib, "ws2_32.lib")

#define HOST "127.0.0.1"
#define PORT 8747

using namespace std;

SOCKET sock;
string ARGS = "";

/////////////////////////////////
// 메인 프로그램 통신 함수 정의
/////////////////////////////////

// UTF-8 인코딩 함수
string utf8_encode(const wstring& wstr) {
	wstring_convert<codecvt_utf8<wchar_t>> conv;
	return conv.to_bytes(wstr);
}

// UTF-8 디코딩 함수
wstring utf8_decode(const string& str) {
	wstring_convert<codecvt_utf8<wchar_t>> conv;
	return conv.from_bytes(str);
}

// 에러 핸들링 함수
void ErrorHandling(const string& message) {
	cerr << "[ERROR] " << message << endl;
	exit(1);
}

// 연결 해제
void closeConn() {
	if (sock != INVALID_SOCKET) {
		closesocket(sock);
		WSACleanup();
		cout << "[STATUS] Connection closed" << endl;
	}
	else {
		cerr << "[ERROR] Network connection has been corrupted." << endl;
	}
}

// 메인 프로그램으로부터 데이터 수신
string receive() {
	char buffer[2048];
	int strLen = recv(sock, buffer, sizeof(buffer) - 1, 0);
	if (strLen <= 0) {
		ErrorHandling("Failed to receive data. Please check if connection to the main program is valid.");
	}
	buffer[strLen] = '\0';
	return string(buffer);
}

// 메인 프로그램으로 데이터(명령어) 전송
string submit(const string& string_to_send) {
	string modified = ARGS + string_to_send + " ";
	if (send(sock, modified.c_str(), modified.length(), 0) == SOCKET_ERROR) {
		ErrorHandling("Failed to send data. Please check if connection to the main program is valid.");
	}
	return receive();
}

// 메인 프로그램 연결 및 초기화
string init(const wstring& nickname) {
	WSADATA wsaData;
	SOCKADDR_IN sockAddr;

	if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0)
		ErrorHandling("WSAStartup failure.");

	sock = socket(PF_INET, SOCK_STREAM, 0);
	if (sock == INVALID_SOCKET)
		ErrorHandling("Socket Creating Failure.");

	memset(&sockAddr, 0, sizeof(sockAddr));
	sockAddr.sin_family = AF_INET;
	sockAddr.sin_addr.s_addr = inet_addr(HOST);
	sockAddr.sin_port = htons(PORT);

	cout << "[STATUS] Trying to connect to " << HOST << ":" << PORT << endl;
	if (connect(sock, (SOCKADDR*)&sockAddr, sizeof(sockAddr)) == SOCKET_ERROR) {
		ErrorHandling("Failed to connect. Please check if the main program is waiting for connection.");
	}

	cout << "[STATUS] Connected" << endl;

	string initCommand = utf8_encode(L"INIT " + nickname);
	return submit(initCommand);
}

/////////////////////////////////
// 입력 데이터 변수 정의
/////////////////////////////////
vector<vector<string>> mapData;                // 맵 정보. 예) mapData[0][1] - [0, 1]의 지형/지물
map<string, vector<string>> myAllies;          // 아군 정보. 예) myAllies["M"] - 플레이어 본인의 정보
map<string, vector<string>> enemies;           // 적군 정보. 예) enemies["X"] - 적 포탑의 정보
vector<string> codes;                          // 주어진 암호문. 예) codes[0] - 첫 번째 암호문

int mapHeight = 0, mapWidth = 0;

/////////////////////////////////
// 입력 데이터 파싱
/////////////////////////////////

// 입력 데이터를 파싱하여 변수에 저장
void parseData(const string& gameData) {
	istringstream iss(gameData);
	string line;

	// 첫 번째 행 데이터 읽기
	getline(iss, line);
	istringstream header(line);
	int numOfAllies, numOfEnemies, numOfCodes;
	header >> mapHeight >> mapWidth >> numOfAllies >> numOfEnemies >> numOfCodes;

	// 기존의 맵 정보를 초기화하고 다시 읽어오기
	mapData.assign(mapHeight, vector<string>(mapWidth));
	for (int i = 0; i < mapHeight; i++) {
		getline(iss, line);
		istringstream row(line);
		for (int j = 0; j < mapWidth; j++) {
			row >> mapData[i][j];
		}
	}

	// 기존의 아군 정보를 초기화하고 다시 읽어오기
	myAllies.clear();
	for (int i = 0; i < numOfAllies; i++) {
		getline(iss, line);
		istringstream allyStream(line);
		string allyName;
		allyStream >> allyName;
		vector<string> allyData;
		string tmp;
		while (allyStream >> tmp) allyData.push_back(tmp);
		myAllies[allyName] = allyData;
	}

	// 기존의 적군 정보를 초기화하고 다시 읽어오기
	enemies.clear();
	for (int i = 0; i < numOfEnemies; i++) {
		getline(iss, line);
		istringstream enemyStream(line);
		string enemyName;
		enemyStream >> enemyName;
		vector<string> enemyData;
		string tmp;
		while (enemyStream >> tmp) enemyData.push_back(tmp);
		enemies[enemyName] = enemyData;
	}

	// 기존의 암호문 정보를 초기화하고 다시 읽어오기
	codes.clear();
	for (int i = 0; i < numOfCodes; i++) {
		getline(iss, line);
		codes.push_back(line);
	}
}

// 파싱한 데이터를 화면에 출력
void printData(const string& gameData) {
	cout << "\n----------입력 데이터----------\n" << gameData << "\n----------------------------\n";

	cout << "\n[맵 정보] (" << mapHeight << " x " << mapWidth << ")\n";
	for (auto& row : mapData) {
		for (auto& cell : row) cout << cell << " ";
		cout << "\n";
	}

	cout << "\n[아군 정보] (아군 수: " << myAllies.size() << ")\n";
	for (auto& kv : myAllies) {
		cout << kv.first << ": ";
		for (auto& v : kv.second) cout << v << " ";
		cout << "\n";
	}

	cout << "\n[적군 정보] (적군 수: " << enemies.size() << ")\n";
	for (auto& kv : enemies) {
		cout << kv.first << ": ";
		for (auto& v : kv.second) cout << v << " ";
		cout << "\n";
	}

	cout << "\n[암호문 정보] (암호문 수: " << codes.size() << ")\n";
	for (auto& code : codes) cout << code << "\n";
}

//////////////////////////////////////
// 알고리즘 함수/메서드 부분 구현 시작
//////////////////////////////////////
const int DIRS[4][2] = { {0,1}, {1,0}, {0,-1}, {-1,0} };
const string MOVE_CMDS[4] = { "R A", "D A", "L A", "U A" };
const string FIRE_CMDS[4] = { "R F", "D F", "L F", "U F" };
const string START_SYMBOL = "M";
const string TARGET_SYMBOL = "X";
const string WALL_SYMBOL = "R";

// BFS 노드 정의
struct BFSNode {
	int row, col;
	vector<string> actions;
	BFSNode(int r, int c, const vector<string>& acts) : row(r), col(c), actions(acts) {}
};

// 경로 탐색 알고리즘
vector<string> bfs(pair<int, int> start, pair<int, int> target) {
	queue<BFSNode> q;
	set<string> visited;

	q.push(BFSNode(start.first, start.second, {}));
	visited.insert(to_string(start.first) + "," + to_string(start.second));

	while (!q.empty()) {
		BFSNode current = q.front();
		q.pop();
		int r = current.row;
		int c = current.col;

		for (int d = 0; d < 4; d++) {
			int nr = r + DIRS[d][0];
			int nc = c + DIRS[d][1];
			if (nr == target.first && nc == target.second) {
				auto result = current.actions;
				result.push_back(FIRE_CMDS[d]);
				return result;
			}
		}

		for (int d = 0; d < 4; d++) {
			int nr = r + DIRS[d][0];
			int nc = c + DIRS[d][1];
			string key = to_string(nr) + "," + to_string(nc);
			if (nr >= 0 && nr < mapHeight && nc >= 0 && nc < mapWidth &&
				mapData[nr][nc] != WALL_SYMBOL && visited.find(key) == visited.end()) {
				visited.insert(key);
				auto newActions = current.actions;
				newActions.push_back(MOVE_CMDS[d]);
				q.push(BFSNode(nr, nc, newActions));
			}
		}
	}
	return {};
}

// 출발지와 목적지의 위치 찾기
pair<pair<int, int>, pair<int, int>> findPositions() {
	pair<int, int> start = { -1,-1 };
	pair<int, int> target = { -1,-1 };
	for (int row = 0; row < mapHeight; row++) {
		for (int col = 0; col < mapWidth; col++) {
			if (mapData[row][col] == START_SYMBOL) start = { row, col };
			if (mapData[row][col] == TARGET_SYMBOL) target = { row, col };
		}
	}
	return { start, target };
}
//////////////////////////////////////
// 알고리즘 함수/메서드 부분 구현 끝
//////////////////////////////////////

int main(int argc, char* argv[]) {
	ARGS = (argc > 1) ? string(argv[1]) : "";

	/////////////////////////////////
	// 닉네임 설정 및 최초 연결
	/////////////////////////////////
	wstring nickname = L"기본코드";
	string gameData = init(nickname);

	/////////////////////////////////
	// 알고리즘 메인 부분 구현 시작
	/////////////////////////////////

	// 최초 데이터 파싱
	parseData(gameData);

	// 출발지점, 목표지점의 위치 확인
	auto positions = findPositions();
	if (positions.first.first == -1 || positions.second.first == -1) {
		cerr << "[ERROR] Start or target not found in map" << endl;
		closeConn();
		return 1;
	}

	// 최초 경로 탐색
	queue<string> actions;
	auto path = bfs(positions.first, positions.second);
	for (auto& act : path) actions.push(act);

	// 반복문: 메인 프로그램 <-> 클라이언트(이 코드) 간 순차로 데이터 송수신(동기 처리)
	while (!gameData.empty()) {

		// 파싱한 데이터를 화면에 출력하여 확인
		printData(gameData);

		// 이전 경로 탐색 결과가 존재하지 않을 경우 다시 탐색
		if (actions.empty()) {
			auto pos = findPositions();
			if (pos.first.first != -1 && pos.second.first != -1) {
				auto path2 = bfs(pos.first, pos.second);
				for (auto& act : path2) actions.push(act);
			}
		}

		// 탱크를 제어할 명령어를 output의 값으로 지정(type: String)
		string output = actions.empty() ? "A" : actions.front();
		if (!actions.empty()) actions.pop();

		// 메인 프로그램에서 명령을 처리할 수 있도록 명령어를 submit()의 인자로 전달
		gameData = submit(output);

		// submit()의 리턴으로 받은 갱신된 데이터를 다시 파싱
		if (!gameData.empty()) {
			parseData(gameData);
		}
	}

	/////////////////////////////////
	// 알고리즘 메인 부분 구현 끝
	/////////////////////////////////

	// 연결 해제
	closeConn();
	return 0;
}
