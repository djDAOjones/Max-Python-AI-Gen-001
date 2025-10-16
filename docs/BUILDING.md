# Building from Source

This document describes how to build the real-time dithering Max/MSP external from source.

## Prerequisites

### Required Software
- **macOS:** 15.6.1 or later
- **Xcode:** Latest stable version (14.0+)
- **Max/MSP:** 8.6.5 or later
- **Max SDK:** Download from [Cycling '74](https://cycling74.com/downloads/sdk)

### Optional Tools
- Git (for cloning the repository)
- Command Line Tools for Xcode

## Setup

### 1. Install Max SDK

1. Download the Max SDK from https://cycling74.com/downloads/sdk
2. Extract to a known location (e.g., `~/Documents/Max_SDK`)
3. Note the path for Xcode configuration

### 2. Clone Repository

```bash
git clone git@github.com:djDAOjones/realtime-dithering-001.git
cd realtime-dithering-001
```

## Building

### Using Xcode (Recommended)

1. Open `realtime-dithering.xcodeproj` in Xcode
2. Configure Max SDK path:
   - Select the project in the navigator
   - Go to Build Settings
   - Update `C74SUPPORT` path to your Max SDK location
3. Select build target: `realtime-dithering` (Release or Debug)
4. Build: Product → Build (⌘B)

The compiled `.mxo` bundle will be in the `build/` directory.

### Using Command Line

```bash
xcodebuild -project realtime-dithering.xcodeproj \
           -scheme realtime-dithering \
           -configuration Release \
           build
```

## Installation

### For Development

Copy the built `.mxo` to your Max externals folder:

```bash
cp -r build/Release/jit.rt.dither.mxo ~/Documents/Max\ 8/Library/
```

### For Distribution

1. Build in Release configuration
2. Test on a clean system
3. Package with help files and examples
4. Create installer or distribute as zip

## Troubleshooting

### Build Errors

**"Max SDK not found"**
- Verify `C74SUPPORT` path in Build Settings
- Ensure Max SDK is properly extracted

**"Code signing failed"**
- Update code signing settings in Xcode
- Use "Sign to Run Locally" for development

**"Architecture mismatch"**
- Ensure building for arm64 (Apple Silicon) or x86_64 (Intel)
- Check Max/MSP architecture requirements

### Runtime Issues

**"External not loading in Max"**
- Check Max console for error messages
- Verify external is in correct location
- Ensure macOS permissions are granted

**"Screen capture not working"**
- Grant Screen Recording permission in System Settings
- Check macOS privacy settings

## Development Workflow

### Debug Build
```bash
xcodebuild -configuration Debug build
```

### Clean Build
```bash
xcodebuild clean
xcodebuild build
```

### Run Tests
```bash
# Tests coming soon
```

## Project Structure

```
realtime-dithering-001/
├── src/                    # Source files
│   ├── main.c             # External entry point
│   ├── screen_capture.c   # Screen capture module
│   ├── dithering.c        # Dithering algorithms
│   └── ...
├── include/               # Header files
├── examples/              # Example Max patches
├── docs/                  # Documentation
└── realtime-dithering.xcodeproj/
```

## Contributing

When contributing code:
1. Follow existing code style
2. Add comments for complex logic
3. Test thoroughly before submitting
4. Update documentation as needed

## Additional Resources

- [Max SDK Documentation](https://cycling74.com/downloads/sdk)
- [Xcode Documentation](https://developer.apple.com/documentation/xcode)
- [Project Plan](../PROJECT_PLAN.md)

---

**Last Updated:** 2025-01-16  
**Status:** In Development
