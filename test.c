#include <stdio.h>
#include <winuser.h>
// #include <unistd.h>

/*
int main(void){
	// printf("Hello, World !\n");
	HWND foreground = GetForegroundWindow();
	// HWND foreground = GetActiveWindow();
	if(foreground){
		char window_title[256];
		GetWindowText(foreground, window_title, 256);
		// GetActiveWindow(foreground, window_title, 256);
		// var a = GetActiveWindow();
		printf("Title: %s\n", window_title);
		// printf("%s?\n", foreground);
	} else {
		printf("Nothing!\n");
	}
}
*/

int main(void){
	while(1){
		HWND foreground = GetForegroundWindow();
		if(foreground){
			char window_title[256];
			GetWindowText(foreground, window_title, 256);
			printf("Title: %s\n", window_title);
		} else {
			printf("Nothing!\n");
		}
	}
}

