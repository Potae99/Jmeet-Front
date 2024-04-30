# Create a heavy text file with 15 characters and a size close to 0.97 megabytes

# Choose characters that occupy multiple bytes
text = "文" * 100000  # Using CJK Unified Ideograph, each character is 3 bytes in UTF-8 encoding
text += "A" * 12000   # Adding some additional bytes with simple characters

# Now, let's make it exactly 15 characters
text = text[:15]

# Writing to file
with open("heavy_text_file.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("Text file created successfully.")
