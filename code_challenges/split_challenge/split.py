errors = ["Oct 12 10:54:04 gonzos-mbp com.apple.xpc.Error: (com.apple.preference.displays.MirrorDisplays): Service only ran for 0 seconds. Pushing respawn out by 10 seconds.",
          "Oct 12 10:54:05 gonzos-mbp Electron[4304].Warning: 17G65: libxpc.dylib + 75013 [0BC7AD67-671D-31D4-8B88-C317B8379598]: 0x89",
          "Oct 12 10:54:14 gonzos-mbp com.apple.xpc.Error: (com.apple.preference.displays.MirrorDisplays): Service only ran for 0 seconds. Pushing respawn out by 10 seconds.",
          "Oct 12 10:54:15 gonzos-mbp Electron[4304].Warning: BUG in libdispatch client: kevent[mach_recv] monitored resource vanished before the source cancel handler was invoked",
          "Oct 12 10:54:24 gonzos-mbp com.apple.xpc.Error: (com.apple.preference.displays.MirrorDisplays): Service only ran for 0 seconds. Pushing respawn out by 10 seconds.",
          "Oct 12 10:54:24 gonzos-mbp com.apple.xpc.Jargon: (com.apple.preference.displays.MirrorDisplays): Service only ran for 0 seconds. Pushing respawn out by 10 seconds."]


for x in errors:
        # if ("Error" in x) or ("Warning" in x):
        if ("Error" in x):
                print(x)
                number = x.count("Error")
