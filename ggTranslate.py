from google.cloud import translate

def translate_text(text, target_language):
    # Khởi tạo client
    client = translate.TranslationServiceClient()

    # Thiết lập thông tin dịch vụ dịch
    parent = client.location_path('your-project-id', 'global')

    # Thiết lập ngôn ngữ nguồn và đích
    target_language_code = target_language.lower()
    contents = [text]
    response = client.translate_text(
        request={
            "parent": parent,
            "target_language_code": target_language_code,
            "contents": contents,
            "mime_type": "text/plain",
        }
    )

    # Trả về kết quả dịch
    translation = response.translations[0]
    return translation.translated_text

# Sử dụng hàm dịch
text_to_translate = "Hello, how are you?"
target_language = "fr"  # Ngôn ngữ đích là tiếng Pháp
translated_text = translate_text(text_to_translate, target_language)
print(translated_text)