#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <locale>
#include <codecvt>

#pragma warning(disable : 4996)
#pragma comment(lib, "ws2_32.lib")

#include <string>
#include <WinSock2.h>

#define HOST "127.0.0.1"
#define PORT 8747

using namespace std;

SOCKET sock;

string utf8_encode(const wstring& wstr) {
	wstring_convert<codecvt_utf8<wchar_t>> conv;
	return conv.to_bytes(wstr);
}

wstring utf8_decode(const string& str) {
	wstring_convert<codecvt_utf8<wchar_t>> conv;
	return conv.from_bytes(str);
}

void ErrorHandling(const string& message) {
	cerr << "[ERROR] " << message << endl;
	exit(1);
}

void close() {
	if (sock != INVALID_SOCKET) {
		closesocket(sock);
		WSACleanup();
		cout << "[STATUS] Connection closed" << endl;
	}
	else {
		cerr << "[ERROR] Network connection has been corrupted." << endl;
	}
}

string submit(const string& string_to_send) {
	string modified = string_to_send + " ";

	if (send(sock, modified.c_str(), modified.length(), 0) == SOCKET_ERROR) {
		ErrorHandling("Failed to send data. Please check if Battle SSAFY is waiting for connection.");
	}

	return "[RESULT] test ok";
}

string init(const wstring& nickname) {
	WSADATA wsaData;
	SOCKADDR_IN sockAddr;
	wstring init_command = L"INIT " + nickname;
	string enc_command = utf8_encode(init_command);

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
		ErrorHandling("Failed to connect. Please check if Battle SSAFY is waiting for connection.");
	}
	else {
		cout << "[STATUS] Connected" << endl;
		return submit(enc_command);
	}

	return "";
}

int main() {
	wstring nickname = L"통신테스트";
	string game_data = init(nickname);

	// while 반복문: 배틀싸피 메인 프로그램과 클라이언트(이 코드)가 데이터를 계속해서 주고받는 부분
	while (!game_data.empty()) {

		// 수신 데이터(입력 데이터) 출력
		cout << game_data << "\n";
		
		// 커맨드 지정
		string output = "A";

		// 커맨드 전송
		game_data = submit(output);

		// 강제 종료(통신테스트용)
		break;
	}

	// 반복문을 빠져나왔을 때 배틀싸피 메인 프로그램과의 연결을 완전히 해제하기 위해 close 함수 호출
	close();
	return 0;
}
