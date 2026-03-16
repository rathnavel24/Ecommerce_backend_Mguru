import cloudinary
import cloudinary.uploader


cloudinary.config(
    cloud_name = "ddmtedwbx",
    api_key = 869552577848573,
    api_secret = "Sm2G4-qpVPXfsPNulYm_jRbvluw"
)
def upload_image(file):
    try :
        image_upload = cloudinary.uploader.upload(file.file)

        return image_upload.get("url")
    except Exception as e:
        raise e
    
    

