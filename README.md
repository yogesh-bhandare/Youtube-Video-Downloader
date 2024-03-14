# YouTube Downloader

This Python application allows you to download YouTube videos and songs using the Pytube library. It was developed to overcome limitations faced with third-party apps and websites, particularly regarding playlist downloading and offline usage.

## Complexities Faced and Solutions:

### Limited Access to Internet:
- **Challenge**: Limited access to Wi-Fi; relied on a mobile data plan with unlimited data at night.
- **Solution**: Developed a script to download YouTube playlists locally during the night.

### Third-Party Website Limitations:
- **Challenge**: Third-party websites lacked playlist downloading options.
- **Solution**: Utilized the Pytube library to create a custom solution for downloading playlists.

### Ordering of Playlist Items:
- **Challenge**: Playlist items were arranged by video title, which wasn't always ideal.
- **Solution**: Implemented a function to rename downloaded videos with an index at the beginning of the title, ensuring proper ordering.

## Usage:

1. Clone the repository:

```bash
git clone https://github.com/your_username/your_project.git
