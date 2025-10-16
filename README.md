# Real-Time Dithering for Max/MSP

A Max/MSP Jitter external that captures a screen area in real-time and outputs a continuously updating dithered image for preview and creative applications.

## Overview

This external allows you to:
- Capture any region of your screen in real-time
- Apply various dithering algorithms to the captured image
- Output the result as a Jitter matrix for further processing
- Control dithering parameters dynamically

## Features

- **Real-time screen capture** using macOS ScreenCaptureKit
- **Multiple dithering algorithms:**
  - Floyd-Steinberg error diffusion
  - Ordered (Bayer) dithering
  - Atkinson dithering
  - Simple threshold dithering
- **Configurable parameters:**
  - Capture region and frame rate
  - Color palette/bit depth
  - Grayscale or color mode
  - Algorithm-specific settings
- **Optimized for performance** with efficient memory management

## Requirements

- **macOS:** 15.6.1 or later
- **Max/MSP:** 8.6.5 or later
- **Xcode:** Latest stable version (for building from source)

## Installation

### Pre-built Binary
1. Download the latest release from the [Releases page](https://github.com/djDAOjones/realtime-dithering-001/releases)
2. Copy the `.mxo` file to your Max externals folder:
   - `~/Documents/Max 8/Library/` or
   - `/Applications/Max.app/Contents/Resources/C74/externals/`
3. Restart Max/MSP

### Building from Source
See [BUILDING.md](docs/BUILDING.md) for detailed build instructions.

## Usage

### Basic Example

```
[jit.rt.dither @region 0 0 640 480 @algorithm floyd-steinberg @palette 2]
|
[jit.pwindow]
```

### Messages

- `start` - Begin screen capture
- `stop` - Stop screen capture
- `region x y w h` - Set capture region (x, y, width, height)
- `getdisplays` - Output information about available displays

### Attributes

- `@region` (int int int int) - Screen capture region [x, y, width, height]
- `@fps` (int) - Capture frame rate (default: 30)
- `@algorithm` (symbol) - Dithering algorithm: `floyd-steinberg`, `ordered`, `atkinson`, `threshold`
- `@palette` (int) - Number of colors/levels: 2, 4, 8, 16, 256 (default: 2)
- `@grayscale` (int) - Enable grayscale mode: 0 or 1 (default: 1)
- `@threshold` (float) - Threshold value for certain algorithms (0.0-1.0)
- `@enabled` (int) - Enable/disable capture: 0 or 1

## Documentation

- [Project Plan](PROJECT_PLAN.md) - Detailed development roadmap
- [API Reference](docs/API.md) - Complete object reference (coming soon)
- [Examples](examples/) - Example Max patches (coming soon)
- [Cascade Transcripts](docs/transcripts/) - Development session logs

## Development Status

🚧 **Currently in active development** - See [PROJECT_PLAN.md](PROJECT_PLAN.md) for roadmap and progress.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

MIT License - See [LICENSE](LICENSE) for details.

## Acknowledgments

- Built with the Max SDK
- Uses macOS ScreenCaptureKit for screen capture
- Implements classic dithering algorithms from computer graphics literature

## Contact

- **Repository:** https://github.com/djDAOjones/realtime-dithering-001
- **Issues:** https://github.com/djDAOjones/realtime-dithering-001/issues

---

**Version:** 0.1.0-dev  
**Last Updated:** 2025-01-16
