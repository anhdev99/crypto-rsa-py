from rsa_crypto_manager import RSACryptoManager
crypto_manager = RSACryptoManager()
#
pub_cer = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDrMRxAeDMYN7umdUbxkoDu/IS/2sxag4IgfueSgPN/7f5ztMjvbxSsGtom69+CRKpDhmoIEuh12bW4Y1kjOYV5ySYO9BmGVdku2OkQoh6dUlKgaqszSnhMbhkB7t3+iXB85y2llB6XvA2Dqse02CNSqUQvOP4mfIug+Rxn7ZQoMQIDAQAB"
# public_key = CryptoExtension().load_public_key(pub_cer=pub_cer)
#
pri_cer = "MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAOsxHEB4Mxg3u6Z1RvGSgO78hL/azFqDgiB+55KA83/t/nO0yO9vFKwa2ibr34JEqkOGaggS6HXZtbhjWSM5hXnJJg70GYZV2S7Y6RCiHp1SUqBqqzNKeExuGQHu3f6JcHznLaWUHpe8DYOqx7TYI1KpRC84/iZ8i6D5HGftlCgxAgMBAAECgYBqLMeGSz01x6NNKFCYqfzO5uy+9/WdPxU1ulSsjM5giH6AmbLEdK8uawjk3UMPuhPrW/juICsVWO1yilcpUcRxMqbOOkbvQMvLs/nMTsv/MS31uq/vjZPTol4K3HmS7GD9oJis7pkMoMwhNhn7S/TbeVnsZjFbsjhftSUWqqWfKQJBAP9MdsFuOU7eNFSo9xn7Axp2kMtaN2IQ2OpAQvd2ktPSqPRQPNhszbFvh/92PB/BvI/Y0fwych3Q4e0+vb/iN6sCQQDr1oGsk4KJxCIYocT42NfDfNIzFzvJXQpHWXiHVHWKE6BUe4Qd4s4Xn9FAYJoNFxdVt4cdoXIPH6e5BIRnJZOTAkByCVu6h1u96O+DKX5G8qKuPWvsCb5XZaMe79l55FMtnxmtF/I10lQHAATFjbDJlqZ9sqIJfxcOTnG8oZvsjEXFAkBeG/MTEqn8n6+bdLJNOvqen6ihipvo9p+raSCXoDRnLP3FuKQ36NGky7mMnv/aSWSeZ+YbBNmm/1LGme7b2jrRAkAf1DrjL/Ft+zohcsi56521m5lokulOZAFPwo/v+PzTHHo6LHD9bgfhXnwpKqmR2IOl8L+U0Xqa4abJllh9Wyqr"
# private_key = CryptoExtension().load_private_key(key=pri_cer)
# # print(public_key)
clearData = "session_id=0df5d5feb2774fb5b5f1137ffd451ea2&imei=123&pin=1"
sign = crypto_manager.sign(clearData, pri_cer)

verify = crypto_manager.verify(clearData, sign, pub_cer)
print(verify)
encrypt = crypto_manager.encrypt(clearData, pub_cer)
decrypt = crypto_manager.decrypt(encrypt, pri_cer)
print(encrypt)
print(decrypt)
# key_size = 1024
# keys = CryptoExtension().gen_rsa_key(key_size)
# print("Public Key:\n", keys[0])
# print("Private Key:\n", keys[1])