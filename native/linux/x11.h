#pragma once
#include <vector>
#include <xcb/xcb.h>
#include <xcb/xcb_ewmh.h>

namespace priv_os_x11 {
	extern xcb_connection_t* connection;
	extern xcb_window_t rootWindow;
	extern xcb_ewmh_connection_t ewmhConnection;

	/**
	 * Ensure that we have connection to X11
	 */
	void ensureConnection();

	xcb_atom_t getAtom(const char* name);

	/**
	 * Find main X11 window from given pid
	 */
	std::vector<xcb_window_t> findWindowsWithPid(const pid_t pid);
	std::vector<xcb_window_t> findWindowsWithPid(const pid_t pid, const xcb_window_t root);
}