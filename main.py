import yt_dlp

def get_video_details(video_url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'force_generic_extractor': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            
            title = info_dict.get('title', 'N/A')
            description = info_dict.get('description', 'N/A')
            tags = info_dict.get('tags', 'N/A')
            uploader = info_dict.get('uploader', 'N/A')
            upload_date = info_dict.get('upload_date', 'N/A')
            view_count = info_dict.get('view_count', 'N/A')
            like_count = info_dict.get('like_count', 'N/A')
            dislike_count = info_dict.get('dislike_count', 'N/A')
            duration = info_dict.get('duration', 'N/A')
            thumbnail = info_dict.get('thumbnail', 'N/A')
            categories = info_dict.get('categories', 'N/A')
            channel_url = info_dict.get('channel_url', 'N/A')
            playlist_title = info_dict.get('playlist_title', 'N/A')
            playlist_position = info_dict.get('playlist_index', 'N/A')

            # Display details in terminal with underlines
            print("YouTube Video Details")
            print("-" * 40)
            
            print("Title:")
            print(title)
            print("-" * 40)

            print("Description:")
            print(description)
            print("-" * 40)

            print("Uploader:")
            print(uploader)
            print("-" * 40)

            print("Upload Date:")
            print(upload_date)
            print("-" * 40)

            print("View Count:")
            print(view_count)
            print("-" * 40)

            print("Like Count:")
            print(like_count)
            print("-" * 40)

            print("Dislike Count:")
            print(dislike_count)
            print("-" * 40)

            print("Duration (seconds):")
            print(duration)
            print("-" * 40)

            print("Thumbnail URL:")
            print(thumbnail)
            print("-" * 40)

            print("Categories:")
            print(", ".join(categories) if categories else 'N/A')
            print("-" * 40)

            print("Channel URL:")
            print(channel_url)
            print("-" * 40)

            print("Playlist Title:")
            print(playlist_title)
            print("-" * 40)

            print("Playlist Position:")
            print(playlist_position)
            print("-" * 40)

            print("Tags:")
            print(", ".join(tags) if tags else 'N/A')
            print("-" * 40)

    except yt_dlp.DownloadError as e:
        print(f"DownloadError: {e}")
    except yt_dlp.ExtractorError as e:
        print(f"ExtractorError: {e}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    video_url = input("Enter YouTube video or shorts URL: ")
    get_video_details(video_url)

if __name__ == "__main__":
    main()
