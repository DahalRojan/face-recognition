# Face Recognition API

A RESTful face recognition service built with FastAPI that provides endpoints for comparing faces in images. The API supports various input methods including file uploads and URL-based image processing.

## Features

- **Face Comparison**: Compare faces between two images with similarity scoring
- **Multiple Input Methods**: Support for uploaded files and image URLs
- **Facial Landmarks**: Generate facial landmark overlays for visualization
- **Similarity Scoring**: Calculate percentage-based similarity scores
- **RESTful API**: Clean and well-documented REST endpoints
- **Docker Support**: Containerized deployment ready
- **CORS Enabled**: Cross-origin requests supported

## Technology Stack

- **FastAPI**: High-performance web framework
- **face_recognition**: Face detection and recognition library
- **OpenCV**: Image processing and computer vision
- **PIL/Pillow**: Image manipulation
- **dlib**: Machine learning algorithms for face recognition
- **NumPy**: Numerical computing
- **Docker**: Containerization

## Installation

### Prerequisites

- Python 3.10+
- pip
- cmake (for dlib compilation)

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/DahalRojan/face-recognition.git
   cd face-recognition
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables**
   ```bash
   # Create .env file
   echo "HOST=http://localhost:8000" > .env
   ```

5. **Create required directories**
   ```bash
   mkdir -p temp assets/images
   ```

6. **Run the application**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

### Docker Setup

1. **Build the image**
   ```bash
   docker build -t face-recognition-api .
   ```

2. **Run the container**
   ```bash
   docker run -p 9292:9292 face-recognition-api
   ```

## API Endpoints

### Base URL
- Local: `http://localhost:8000`
- Docker: `http://localhost:9292`

### Interactive Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Endpoints

#### 1. Compare Two Uploaded Images
```http
POST /face-recognition/verify/image2image
```

**Parameters:**
- `image1`: First image file (multipart/form-data)
- `image2`: Second image file (multipart/form-data)

**Example using curl:**
```bash
curl -X POST "http://localhost:8000/face-recognition/verify/image2image" \
  -F "image1=@path/to/first/image.jpg" \
  -F "image2=@path/to/second/image.jpg"
```

#### 2. Compare Uploaded Image with URL Image
```http
POST /face-recognition/verify/image2url
```

**Parameters:**
- `image`: Image file (multipart/form-data)
- `url`: Image URL (string)

**Example using curl:**
```bash
curl -X POST "http://localhost:8000/face-recognition/verify/image2url" \
  -F "image=@path/to/image.jpg" \
  -F "url=https://example.com/image.jpg"
```

#### 3. Compare Two URL Images
```http
POST /face-recognition/verify/url2url
```

**Parameters:**
- `url1`: First image URL (string)
- `url2`: Second image URL (string)

**Example using curl:**
```bash
curl -X POST "http://localhost:8000/face-recognition/verify/url2url" \
  -H "Content-Type: application/json" \
  -d '{
    "url1": "https://example.com/image1.jpg",
    "url2": "https://example.com/image2.jpg"
  }'
```

#### 4. Get Processed Images
```http
GET /images/{filename}
```

Access processed images and facial landmark overlays.

## Response Format

All face comparison endpoints return the following JSON structure:

```json
{
  "is_similar": true,
  "similarity": 87.5,
  "match_index": 1,
  "nfaces": 1,
  "image1": "http://localhost:8000/images/image_abc123.png",
  "image1_landmark": "http://localhost:8000/images/image_def456.png",
  "image2": "http://localhost:8000/images/image_ghi789.png",
  "image2_landmark": "http://localhost:8000/images/image_jkl012.png"
}
```

**Response Fields:**
- `is_similar`: Boolean indicating if faces match
- `similarity`: Percentage similarity score (0-100)
- `match_index`: Index of the matched face
- `nfaces`: Number of faces detected in the reference image
- `image1`: URL to the first processed image
- `image1_landmark`: URL to the first image with facial landmarks
- `image2`: URL to the second processed image
- `image2_landmark`: URL to the second image with facial landmarks

## Configuration

### Environment Variables

- `HOST`: Base URL for serving images (default: `http://localhost:8000`)

### Face Recognition Settings

- **Tolerance**: Default tolerance is `0.45` (configurable in `ai/recognition/core.py`)
- **Supported Formats**: JPEG, PNG, BMP, TIFF

## Project Structure

```
face-recognition/
├── main.py                 # FastAPI application entry point
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker configuration
├── .gitignore             # Git ignore patterns
├── README.md              # Project documentation
└── ai/
    ├── core/              # Core utilities
    │   ├── settings.py    # Configuration settings
    │   ├── routers.py     # Router initialization
    │   ├── views.py       # Image serving endpoints
    │   ├── file.py        # File handling utilities
    │   ├── image.py       # Image processing utilities
    │   └── utils.py       # Helper functions
    └── recognition/       # Face recognition module
        ├── core.py        # Main recognition logic
        ├── views.py       # API endpoints
        ├── schemas.py     # Pydantic models
        └── version.py     # Version information
```

## Error Handling

The API returns appropriate HTTP status codes:

- `200`: Success
- `400`: Bad request (invalid image format, missing parameters)
- `404`: No face found in image
- `424`: Failed to download image from URL
- `500`: Internal server error

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For issues and questions:
- Create an issue on GitHub
- Check the API documentation at `/docs`

## Changelog

### Version 2.0
- Improved API title and documentation
- Enhanced error handling and messages
- Added configuration constants
- Fixed BASE_DIR path resolution
- Added comprehensive .gitignore

### Version 1.0
- Initial release
- Basic face recognition functionality
- Docker support
- RESTful API endpoints