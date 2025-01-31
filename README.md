# RSACryptoManager
RSAEncryptionHandler là một module Python cho phép thực hiện các thao tác mã hóa và giải mã bằng RSA. Module này sử dụng thư viện `cryptography` để cung cấp các chức năng chính bao gồm mã hóa, giải mã, tạo khóa RSA, ký và xác minh chữ ký số.

### Author: Anhdev99

### Website: https://anhdev99.com


## Cài đặt

Trước khi sử dụng module, bạn cần cài đặt thư viện `cryptography`:

```bash
pip install cryptography
```

## Sử dụng

### 1. Tạo một đối tượng RSACryptoManager

```python
from rsa_crypto_manager import RSACryptoManager

crypto = RSACryptoManager()
```

### 2. Tạo cặp khóa RSA

```python
public_key, private_key = crypto.gen_rsa_key(key_size=2048)
```


### 3. Mã hóa dữ liệu
```python
data_to_encrypt = "Hello, World!"
encrypted_data = crypto.encrypt(data_to_encrypt, public_key)
print(f"Encrypted Data: {encrypted_data}")
```

### 4. Giải mã dữ liệu
```python
decrypted_data = crypto.decrypt(encrypted_data, private_key)
print(f"Decrypted Data: {decrypted_data}")
```

### 5. Ký dữ liệu
```python
data_to_sign = "Important message"
signature = crypto.sign(data_to_sign, private_key)
print(f"Signature: {signature}")
```

### 6. Xác minh chữ ký
```python
is_valid = crypto.verify(data_to_sign, signature, public_key)
print(f"Signature valid: {is_valid}")
```

## Các hàm trong module

### `gen_rsa_key(key_size: int) -> [str, str]`

Tạo một cặp khóa RSA.

- `key_size`: Kích thước của khóa (ví dụ: 2048).
- Trả về: Một danh sách chứa khóa công khai và khóa riêng tư dưới dạng chuỗi đã mã hóa Base64.

### `encrypt(data_to_encrypt: str, pub_cer: str) -> str`

Mã hóa dữ liệu bằng khóa công khai.

- `data_to_encrypt`: Dữ liệu cần mã hóa.
- `pub_cer`: Khóa công khai dưới dạng chuỗi Base64.
- Trả về: Dữ liệu đã mã hóa dưới dạng chuỗi Base64.

### `decrypt(data_encrypted: str, priv_key_pem: str) -> str`

Giải mã dữ liệu bằng khóa riêng tư.

- `data_encrypted`: Dữ liệu đã mã hóa dưới dạng chuỗi Base64.
- `priv_key_pem`: Khóa riêng tư dưới dạng chuỗi Base64.
- Trả về: Dữ liệu đã giải mã dưới dạng chuỗi.

### `sign(data_to_sign: str, private_key: str, is_file: bool = False) -> str`

Ký dữ liệu bằng khóa riêng tư.

- `data_to_sign`: Dữ liệu cần ký.
- `private_key`: Khóa riêng tư dưới dạng chuỗi Base64.
- `is_file`: (Tùy chọn) Chỉ định nếu `private_key` là đường dẫn tới file chứa khóa.
- Trả về: Chữ ký số dưới dạng chuỗi Base64.

### `verify(data_to_verify: str, signed_data: str, pub_cer: str, is_file: bool = False) -> bool`

Xác minh chữ ký số bằng khóa công khai.

- `data_to_verify`: Dữ liệu cần xác minh.
- `signed_data`: Chữ ký số dưới dạng chuỗi Base64.
- `pub_cer`: Khóa công khai dưới dạng chuỗi Base64.
- `is_file`: (Tùy chọn) Chỉ định nếu `pub_cer` là đường dẫn tới file chứa khóa.
- Trả về: `True` nếu chữ ký hợp lệ, `False` nếu không hợp lệ.