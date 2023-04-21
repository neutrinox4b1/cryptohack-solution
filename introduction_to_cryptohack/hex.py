cipher = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
plain = "crypto{You_will_be_working_with_hex_strings_a_lot}"

print(bytes.hex(bytes(plain, "utf-8")))
print(bytes.fromhex(cipher))

#bytes.hex와 bytes.fromhex의 사용. bytes(plain, 'utf-8')은 string을 bytes로 변환하는데 사용함.