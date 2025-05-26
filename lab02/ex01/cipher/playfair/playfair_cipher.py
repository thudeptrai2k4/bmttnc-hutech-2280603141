class PlayFairCipher:
    def __init__(self):
        pass
    
    def create_playfair_matrix(self, key):
        key = key.replace("J", "I").upper()
        key_set = set()
        matrix = []
        
        # Add unique letters from key to matrix
        for char in key:
            if char not in key_set and char.isalpha():
                key_set.add(char)
                matrix.append(char)
        
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 'J' omitted, 'V' included properly
        
        # Add remaining letters not in key
        for letter in alphabet:
            if letter not in key_set:
                matrix.append(letter)
                if len(matrix) == 25:
                    break
        
        # Convert list to 5x5 matrix
        playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix
    
    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        return None, None  # In case letter not found
    
    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace("J", "I").upper()
        encrypted_text = ""
        i = 0
        while i < len(plain_text):
            a = plain_text[i]
            b = ''
            if i + 1 < len(plain_text):
                b = plain_text[i + 1]
            
            if b == '' or a == b:
                b = 'X'
                i += 1
            else:
                i += 2
            
            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)
            
            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
        
        return encrypted_text
    
    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""
        for i in range(0, len(cipher_text), 2):
            a = cipher_text[i]
            b = cipher_text[i + 1]
            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)
            
            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]
        
        # Remove padding X's that were inserted between repeated letters
        result = ""
        i = 0
        while i < len(decrypted_text):
            result += decrypted_text[i]
            if (i + 2 < len(decrypted_text) and
                decrypted_text[i] == decrypted_text[i + 2] and
                decrypted_text[i + 1] == 'X'):
                i += 2  # Skip the 'X'
            else:
                i += 1
        
        # Remove trailing 'X' if it was padding at the end
        if result.endswith('X'):
            result = result[:-1]
        
        return result
