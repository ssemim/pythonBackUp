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

void ErrorHandling(const char* message) {
	fprintf(stderr, "[ERROR] %s\n", message);
	exit(1);
}

char* utf8_encode(const wchar_t* wstr) {
	int size_needed = WideCharToMultiByte(CP_UTF8, 0, wstr, -1, NULL, 0, NULL, NULL);
	char* str_to = (char*)malloc(size_needed);
	WideCharToMultiByte(CP_UTF8, 0, wstr, -1, str_to, size_needed, NULL, NULL);
	return str_to;
}

wchar_t* utf8_decode(const char* str) {
	int size_needed = MultiByteToWideChar(CP_UTF8, 0, str, -1, NULL, 0);
	wchar_t* wstr_to = (wchar_t*)malloc(size_needed * sizeof(wchar_t));
	MultiByteToWideChar(CP_UTF8, 0, str, -1, wstr_to, size_needed);
	return wstr_to;
}

void close() {
	if (sock != INVALID_SOCKET) {
		closesocket(sock);
		WSACleanup();
		printf("[STATUS] Connection closed\n");
	}
	else {
		fprintf(stderr, "[ERROR] Network connection has been corrupted.\n");
	}
}

char* submit(const char* string_to_send) {
	char buffer[1024];
	snprintf(buffer, sizeof(buffer), "%s ", string_to_send);

	if (send(sock, buffer, strlen(buffer), 0) == SOCKET_ERROR) {
		ErrorHandling("Failed to send data. Please check if Battle SSAFY is waiting for connection.");
	}

	return "[RESULT] test ok";
}

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
		ErrorHandling("Failed to connect. Please check if Battle SSAFY is waiting for connection.");
	}
	else {
		printf("[STATUS] Connected\n");
		return submit(enc_command);
	}

	free(enc_command);
	return NULL;
}

int main() {
	wchar_t nickname[] = L"통신테스트";
	char* game_data = init(nickname);

	// while 반복문: 배틀싸피 메인 프로그램과 클라이언트(이 코드)가 데이터를 계속해서 주고받는 부분
	while (game_data != NULL)
	{
		// 수신 데이터(입력 데이터) 출력
		printf("%s\n", game_data);

		// 커맨드 지정
		char output[] = "A";

		// 커맨드 전송
		submit(output);

		// 강제 종료(통신테스트용)
		break;
	}

	close();
	return 0;
}
