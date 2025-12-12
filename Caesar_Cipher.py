def caesar_encrypt(message, shift):
    """
    Encrypts a message using Caesar Cipher
    """
    encrypted = ""
    
    for char in message:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            ascii_offset = ord('A') if char.isupper() else ord('a')
            
            # Apply the shift and wrap around using modulo 26
            shifted = (ord(char) - ascii_offset + shift) % 26
            encrypted += chr(shifted + ascii_offset)
        else:
            # Keep non-alphabetic characters unchanged
            encrypted += char
    
    return encrypted

def caesar_decrypt(message, shift):
    """
    Decrypts a message using Caesar Cipher
    """
    # Decryption is just encryption with negative shift
    return caesar_encrypt(message, -shift)

def get_user_input():
    """
    Gets input from user and validates it
    """
    while True:
        try:
            print("\n" + "="*50)
            print("CAESAR CIPHER ENCRYPTION/DECRYPTION")
            print("="*50)
            print("1. Encrypt a message")
            print("2. Decrypt a message")
            print("3. Exit")
            print("-"*50)
            
            choice = input("Enter your choice (1/2/3): ").strip()
            
            if choice == '3':
                return None, None, None
            
            if choice not in ['1', '2']:
                print("❌ Invalid choice! Please enter 1, 2, or 3.")
                continue
            
            message = input("Enter your message: ")
            
            # Get shift value (handling both positive and negative)
            shift_input = input("Enter shift value (0-25, or any integer): ").strip()
            shift = int(shift_input) % 26  # Normalize to 0-25 range
            
            return choice, message, shift
            
        except ValueError:
            print("❌ Invalid shift value! Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\n\n👋 Program terminated by user.")
            return None, None, None

def main():
    """
    Main function to run the Caesar Cipher program
    """
    print("🔐 Welcome to Caesar Cipher Tool!")
    print("   This program encrypts and decrypts text using the Caesar Cipher algorithm.")
    
    while True:
        choice, message, shift = get_user_input()
        
        # Exit condition
        if choice is None:
            print("👋 Thank you for using Caesar Cipher! Goodbye!")
            break
        
        try:
            if choice == '1':
                # Encrypt
                result = caesar_encrypt(message, shift)
                print(f"\n✅ ENCRYPTION RESULT:")
                print(f"   Original: {message}")
                print(f"   Shift: {shift}")
                print(f"   Encrypted: {result}")
                
            elif choice == '2':
                # Decrypt
                result = caesar_decrypt(message, shift)
                print(f"\n✅ DECRYPTION RESULT:")
                print(f"   Encrypted: {message}")
                print(f"   Shift: {shift}")
                print(f"   Decrypted: {result}")
            
            # Ask if user wants to continue
            print("\n" + "-"*50)
            continue_choice = input("Do you want to perform another operation? (y/n): ").strip().lower()
            if continue_choice not in ['y', 'yes', '']:
                print("👋 Thank you for using Caesar Cipher! Goodbye!")
                break
                
        except Exception as e:
            print(f"❌ An error occurred: {e}")

# Additional utility functions
def demo_caesar_cipher():
    """
    Demonstrates Caesar Cipher with examples
    """
    print("\n📊 DEMONSTRATION EXAMPLES:")
    print("-" * 30)
    
    examples = [
        ("HELLO WORLD", 3),
        ("python123", 7),
        ("Caesar Cipher!", 13)
    ]
    
    for msg, shift in examples:
        encrypted = caesar_encrypt(msg, shift)
        decrypted = caesar_decrypt(encrypted, shift)
        print(f"Original: '{msg}'")
        print(f"Shift: {shift}")
        print(f"Encrypted: '{encrypted}'")
        print(f"Decrypted: '{decrypted}'")
        print("-" * 30)

def brute_force_decrypt(message):
    """
    Try all possible shifts (0-25) to decrypt a message
    """
    print(f"\n🔍 BRUTE FORCE DECRYPTION for: '{message}'")
    print("-" * 40)
    
    for shift in range(26):
        decrypted = caesar_decrypt(message, shift)
        print(f"Shift {shift:2d}: {decrypted}")

if __name__ == "__main__":
    # Optional: Uncomment the next line to see demonstration examples
    # demo_caesar_cipher()
    
    # Run the main program
    main()