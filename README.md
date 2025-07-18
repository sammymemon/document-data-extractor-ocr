# Document Data Extractor

A modern web application that extracts data from images and PDF documents using OCR (Optical Character Recognition) technology. Built with Next.js, TypeScript, and PaddleOCR.

## Features

- **Multi-file Upload**: Upload multiple images (JPG, PNG, BMP, TIFF) and PDF files
- **OCR Processing**: Extract text data using PaddleOCR
- **Data Extraction**: Automatically extract vendor names, document types, PO numbers, bill numbers, dates, amounts, and project names
- **Company Verification**: Verify company names against predefined list ("dev accelerator limited" and "needle and thread llp")
- **Manual Signing Status**: Manually update signing status (Yes/No) for each document
- **Modern UI**: Clean, responsive interface built with Tailwind CSS and shadcn/ui components

## Table Columns

The extracted data is displayed in a table with the following columns:

- File Name
- Status
- Vendor Name
- Document Type
- PO Number
- Bill Number
- Bill Date
- Total Amount
- Project Name
- Signed? (Manual dropdown: Yes/No)
- Details/Error
- Company Name Verified

## Setup Instructions

### Prerequisites

- Node.js (v18 or higher)
- Python 3.7 or higher
- npm or yarn

### Installation

1. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

2. **Install Python dependencies:**
   ```bash
   pip install paddleocr pdf2image Pillow
   ```
   
   Or using the requirements file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure Python is accessible:**
   Make sure `python3` command is available in your system PATH. The application uses `python3` to run the OCR script.

### Running the Application

1. **Start the development server:**
   ```bash
   npm run dev
   ```

2. **Open your browser:**
   Navigate to [http://localhost:8000](http://localhost:8000) to access the application.

## Usage

1. **Upload Files**: Click on the file input to select multiple images or PDF files
2. **Extract Data**: Click the "Extract Data" button to process the files
3. **Review Results**: View the extracted data in the table below
4. **Update Signing Status**: Use the dropdown in the "Signed?" column to manually update the signing status
5. **Verify Company Names**: Check the "Company Name Verified" column to see if vendor names match the predefined companies

## Technical Architecture

### Backend (Next.js API)
- **API Endpoint**: `/api/extractdata`
- **File Processing**: Uses formidable for multipart form data handling
- **OCR Integration**: Spawns Python process to run PaddleOCR script
- **Data Extraction**: Regex-based extraction of specific fields from OCR text

### Frontend (Next.js + React)
- **File Upload**: Modern file input with drag-and-drop support
- **Real-time Updates**: Loading states and error handling
- **Responsive Table**: Displays extracted data with manual editing capabilities
- **Clean UI**: Built with Tailwind CSS and shadcn/ui components

### Python OCR Script
- **PaddleOCR**: Advanced OCR engine for text extraction
- **Error Handling**: Comprehensive error handling and JSON output
- **Multi-format Support**: Handles images and PDFs

## File Structure

```
├── ocr/
│   └── ocr_extract.py          # Python OCR script
├── src/
│   ├── app/
│   │   ├── api/
│   │   │   └── extractdata/
│   │   │       └── route.ts    # API endpoint for file processing
│   │   ├── layout.tsx          # Root layout
│   │   ├── page.tsx            # Main upload and results page
│   │   └── globals.css         # Global styles
│   └── components/ui/          # shadcn/ui components
├── requirements.txt            # Python dependencies
└── package.json               # Node.js dependencies
```

## Error Handling

- **File Type Validation**: Only accepts supported image and PDF formats
- **Size Limits**: 10MB maximum file size per upload
- **OCR Errors**: Graceful handling of OCR processing failures
- **Network Errors**: Proper error messages for API failures

## Deployment Notes

- Ensure Python and required packages are installed on the deployment server
- Configure proper file upload limits in your hosting environment
- Set appropriate timeout values for OCR processing

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.
\
