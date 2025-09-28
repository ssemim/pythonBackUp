#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <wchar.h>
#include <winsock2.h>

#pragma warning(disable : 4996)
#pragma comment(lib, "ws2_32.lib")

#define HOST "127.0.0.1"
#define PORT 8747

SOCKET sock;
char ARGS[256] = "";

/////////////////////////////////
// 메인 프로그램 통신 함수 정의
/////////////////////////////////

// UTF-8 인코딩 함수
char* utf8_encode(const wchar_t* wstr) {
	int size_needed = WideCharToMultiByte(CP_UTF8, 0, wstr, -1, NULL, 0, NULL, NULL);
	char* str_to = (char*)malloc(size_needed);
	WideCharToMultiByte(CP_UTF8, 0, wstr, -1, str_to, size_needed, NULL, NULL);
	return str_to;
}

// UTF-8 디코딩 함수
wchar_t* utf8_decode(const char* str) {
	int size_needed = MultiByteToWideChar(CP_UTF8, 0, str, -1, NULL, 0);
	wchar_t* wstr_to = (wchar_t*)malloc(size_needed * sizeof(wchar_t));
	MultiByteToWideChar(CP_UTF8, 0, str, -1, wstr_to, size_needed);
	return wstr_to;
}

// 에러 핸들링 함수
void ErrorHandling(const char* message) {
	fprintf(stderr, "[ERROR] %s\n", message);
	exit(1);
}

// 연결 해제
void closeConn() {
	if (sock != INVALID_SOCKET) {
		closesocket(sock);
		WSACleanup();
		printf("[STATUS] Connection closed\n");
	}
	else {
		fprintf(stderr, "[ERROR] Network connection has been corrupted.\n");
	}
}

// 메인 프로그램으로부터 데이터 수신
char* receive() {
	char buffer[2048];
	int strLen = recv(sock, buffer, sizeof(buffer) - 1, 0);
	if (strLen <= 0) {
		ErrorHandling("Failed to receive data. Please check if connection to the main program is valid.");
	}
	buffer[strLen] = '\0';
	return _strdup(buffer);  // strdup으로 안전하게 복사
}

// 메인 프로그램으로 데이터(명령어) 전송
char* submit(const char* string_to_send) {
	char buffer[1024];
	snprintf(buffer, sizeof(buffer), "%s%s ", ARGS, string_to_send);

	if (send(sock, buffer, strlen(buffer), 0) == SOCKET_ERROR) {
		ErrorHandling("Failed to send data. Please check if connection to the main program is valid.");
	}
	return receive();
}

// 메인 프로그램 연결 및 초기화
char* init(const wchar_t* nickname) {
	WSADATA wsaData;
	SOCKADDR_IN sockAddr;
	wchar_t init_command[256] = L"INIT ";
	wcscat(init_command, nickname);
	char* enc_command = utf8_encode(init_command);

	if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0)
		ErrorHandling("WSAStartup failure.");

	sock = socket(PF_INET, SOCK_STREAM, 0);
	if (sock == INVALID_SOCKET)
		ErrorHandling("Socket Creating Failure.");

	memset(&sockAddr, 0, sizeof(sockAddr));
	sockAddr.sin_family = AF_INET;
	sockAddr.sin_addr.s_addr = inet_addr(HOST);
	sockAddr.sin_port = htons(PORT);

	printf("[STATUS] Trying to connect to %s:%d\n", HOST, PORT);
	if (connect(sock, (SOCKADDR*)&sockAddr, sizeof(sockAddr)) == SOCKET_ERROR) {
		ErrorHandling("Failed to connect. Please check if the main program is waiting for connection.");
	}

	printf("[STATUS] Connected\n");
	char* result = submit(enc_command);
	free(enc_command);
	return result;
}

/////////////////////////////////
// 최대 사이즈 정의
/////////////////////////////////
#define MAX_ROWS 100
#define MAX_COLS 100
#define MAX_LEN 10
#define MAX_ALLIES 100
#define MAX_ENEMIES 100
#define MAX_CODES 100
#define MAX_ACTIONS 200

/////////////////////////////////
// 입력 데이터 변수 정의
/////////////////////////////////
int map_height, map_width, num_of_allies, num_of_enemies, num_of_codes;
char lines[MAX_ROWS][MAX_LEN * MAX_COLS];
char map_data[MAX_ROWS][MAX_COLS][MAX_LEN];
char my_allies[MAX_ALLIES][MAX_COLS][MAX_LEN];
char enemies[MAX_ENEMIES][MAX_COLS][MAX_LEN];
char codes[MAX_CODES][MAX_LEN];

/////////////////////////////////
// 입력 데이터 파싱
/////////////////////////////////

// 입력 데이터를 파싱하여 변수에 저장
void parse_data(char* game_data) {
	int line_index = 0;
	char* token = strtok(game_data, "\n");
	while (token != NULL) {
		strncpy(lines[line_index], token, sizeof(lines[line_index]) - 1);
		lines[line_index][sizeof(lines[line_index]) - 1] = '\0';
		line_index++;
		token = strtok(NULL, "\n");
	}

	// 첫 번째 행 데이터 읽기
	sscanf(lines[0], "%d %d %d %d %d", &map_height, &map_width, &num_of_allies, &num_of_enemies, &num_of_codes);

	// 기존의 맵 정보를 초기화하고 다시 읽어오기
	for (int i = 0; i < map_height; i++) {
		char* t = strtok(lines[i + 1], " ");
		for (int j = 0; j < map_width; j++) {
			if (t != NULL) {
				strncpy(map_data[i][j], t, MAX_LEN - 1);
				map_data[i][j][MAX_LEN - 1] = '\0';
				t = strtok(NULL, " ");
			}
		}
	}

	// 기존의 아군 정보를 초기화하고 다시 읽어오기
	for (int i = 0; i < num_of_allies; i++) {
		char* t = strtok(lines[map_height + 1 + i], " ");
		int j = 0;
		while (t != NULL) {
			strncpy(my_allies[i][j], t, MAX_LEN - 1);
			my_allies[i][j][MAX_LEN - 1] = '\0';
			t = strtok(NULL, " ");
			j++;
		}
	}

	// 기존의 적군 정보를 초기화하고 다시 읽어오기
	for (int i = 0; i < num_of_enemies; i++) {
		char* t = strtok(lines[map_height + 1 + num_of_allies + i], " ");
		int j = 0;
		while (t != NULL) {
			strncpy(enemies[i][j], t, MAX_LEN - 1);
			enemies[i][j][MAX_LEN - 1] = '\0';
			t = strtok(NULL, " ");
			j++;
		}
	}

	// 기존의 암호문 정보를 초기화하고 다시 읽어오기
	for (int i = 0; i < num_of_codes; i++) {
		strncpy(codes[i], lines[map_height + 1 + num_of_allies + num_of_enemies + i], MAX_LEN - 1);
		codes[i][MAX_LEN - 1] = '\0';
	}
}

// 파싱한 데이터를 화면에 출력
void print_data(const char* game_data) {
	printf("\n----------입력 데이터----------\n%s\n----------------------------\n", game_data);

	printf("\n[맵 정보] (%d x %d)\n", map_height, map_width);
	for (int i = 0; i < map_height; i++) {
		for (int j = 0; j < map_width; j++) {
			printf("%s ", map_data[i][j]);
		}
		printf("\n");
	}

	printf("\n[아군 정보] (아군 수: %d)\n", num_of_allies);
	for (int i = 0; i < num_of_allies; i++) {
		int j = 0;
		while (strlen(my_allies[i][j]) > 0) {
			printf("%s ", my_allies[i][j]);
			j++;
		}
		printf("\n");
	}

	printf("\n[적군 정보] (적군 수: %d)\n", num_of_enemies);
	for (int i = 0; i < num_of_enemies; i++) {
		int j = 0;
		while (strlen(enemies[i][j]) > 0) {
			printf("%s ", enemies[i][j]);
			j++;
		}
		printf("\n");
	}

	printf("\n[암호문 정보] (암호문 수: %d)\n", num_of_codes);
	for (int i = 0; i < num_of_codes; i++) {
		printf("%s\n", codes[i]);
	}
}

////////////////////////////////////////
// 알고리즘 함수/메서드 부분 구현 시작
////////////////////////////////////////
const int DIRS[4][2] = { {0,1}, {1,0}, {0,-1}, {-1,0} };
const char* MOVE_CMDS[4] = { "R A", "D A", "L A", "U A" };
const char* FIRE_CMDS[4] = { "R F", "D F", "L F", "U F" };
const char* START_SYMBOL = "M";
const char* TARGET_SYMBOL = "X";
const char* WALL_SYMBOL = "R";

// BFS 노드 정의
typedef struct {
	int row, col;
	char actions[MAX_ACTIONS][10];
	int action_count;
} BFSNode;

// BFS 큐 정의
typedef struct {
	BFSNode data[MAX_ACTIONS];
	int front, rear;
} Queue;

// BFS 큐 검사 및 제어 함수
void init_queue(Queue* q) { q->front = q->rear = 0; }
int is_empty(Queue* q) { return q->front == q->rear; }
void enqueue(Queue* q, BFSNode node) { q->data[q->rear] = node; q->rear = (q->rear + 1) % MAX_ACTIONS; }
BFSNode dequeue(Queue* q) { BFSNode n = q->data[q->front]; q->front = (q->front + 1) % MAX_ACTIONS; return n; }

int visited[MAX_ROWS][MAX_COLS];

// 경로 탐색 알고리즘
int bfs(int sr, int sc, int tr, int tc, char actions[][10], int* action_count) {
	Queue q; init_queue(&q);

	for (int i = 0; i < MAX_ROWS; i++)
		for (int j = 0; j < MAX_COLS; j++)
			visited[i][j] = 0;

	BFSNode start = { sr, sc, {""}, 0 };
	enqueue(&q, start);
	visited[sr][sc] = 1;

	while (!is_empty(&q)) {
		BFSNode cur = dequeue(&q);

		for (int d = 0; d < 4; d++) {
			int nr = cur.row + DIRS[d][0];
			int nc = cur.col + DIRS[d][1];
			if (nr == tr && nc == tc) {
				*action_count = cur.action_count;
				for (int i = 0; i < cur.action_count; i++)
					strcpy(actions[i], cur.actions[i]);
				strcpy(actions[*action_count], FIRE_CMDS[d]);
				(*action_count)++;
				return 1;
			}
		}

		for (int d = 0; d < 4; d++) {
			int nr = cur.row + DIRS[d][0];
			int nc = cur.col + DIRS[d][1];
			if (nr >= 0 && nr < map_height && nc >= 0 && nc < map_width &&
				strcmp(map_data[nr][nc], WALL_SYMBOL) != 0 && !visited[nr][nc]) {
				visited[nr][nc] = 1;
				BFSNode next = cur;
				next.row = nr; next.col = nc;
				strcpy(next.actions[next.action_count], MOVE_CMDS[d]);
				next.action_count++;
				enqueue(&q, next);
			}
		}
	}
	return 0;
}

// 출발지와 목적지의 위치 찾기
int find_positions(int* sr, int* sc, int* tr, int* tc) {
	*sr = *sc = *tr = *tc = -1;
	for (int r = 0; r < map_height; r++) {
		for (int c = 0; c < map_width; c++) {
			if (strcmp(map_data[r][c], START_SYMBOL) == 0) {
				*sr = r; *sc = c;
			}
			else if (strcmp(map_data[r][c], TARGET_SYMBOL) == 0) {
				*tr = r; *tc = c;
			}
		}
	}
	return (*sr != -1 && *tr != -1);
}
////////////////////////////////////////
// 알고리즘 함수/메서드 부분 구현 끝
////////////////////////////////////////

int main(int argc, char* argv[]) {
	if (argc > 1) strncpy(ARGS, argv[1], sizeof(ARGS) - 1);

	//////////////////////////////////
	// 닉네임 설정 및 최초 연결
	//////////////////////////////////
	wchar_t NICKNAME[] = L"기본코드";
	char* game_data = init(NICKNAME);

	//////////////////////////////////
	// 알고리즘 메인 부분 구현 시작
	//////////////////////////////////

	// 최초 데이터 파싱
	parse_data(game_data);

	// 출발지점, 목표지점의 위치 확인
	int sr, sc, tr, tc;
	if (!find_positions(&sr, &sc, &tr, &tc)) {
		printf("[ERROR] Start or target not found in map\n");
		closeConn();
		return 1;
	}

	// 최초 경로 탐색
	char actions[MAX_ACTIONS][10];
	int action_count = 0, action_index = 0;
	if (bfs(sr, sc, tr, tc, actions, &action_count)) {
		action_index = 0;
	}

	// 반복문: 메인 프로그램 <-> 클라이언트(이 코드) 간 순차로 데이터 송수신(동기 처리)
	while (game_data != NULL) {

		// 파싱한 데이터를 화면에 출력하여 확인 후 메모리 해제
		print_data(game_data);
		free(game_data);
		game_data = NULL;

		// 이전 경로 탐색 결과가 존재하지 않을 경우 다시 탐색
		if (action_index >= action_count) {
			if (find_positions(&sr, &sc, &tr, &tc)) {
				if (bfs(sr, sc, tr, tc, actions, &action_count)) {
					action_index = 0;
				}
			}
		}

		// 탱크를 제어할 명령어를 output의 값으로 지정(type: char[])
		char output[128];
		if (action_index < action_count) {
			strcpy(output, actions[action_index]);
			action_index++;
		}
		else {
			strcpy(output, "A");
		}

		// 메인 프로그램에서 명령을 처리할 수 있도록 명령어를 submit()의 인자로 전달
		game_data = submit(output);

		// submit()의 리턴으로 받은 갱신된 데이터를 다시 파싱
		if (game_data != NULL) {
			parse_data(game_data);
		}
	}

	//////////////////////////////////
	// 알고리즘 메인 부분 구현 끝
	//////////////////////////////////

	closeConn();
	return 0;
}
