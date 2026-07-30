import streamlit as st
from Crypto.Cipher import AES

st.title("Expérience 1 — Chiffrement symétrique AES")

# Clé secrète partagée et fixe pour l'exercice (16 octets)
CLE_SECRETE = b'MonSuperSecret09'

tab1, tab2, tab3 = st.tabs(["Essai A", "Essai B", "Essai C"])

# --- Essai A : Clé inconnue d'Eve ---
with tab1:
    st.header("Essai A — Clé inconnue d'Eve")
    message_a = st.text_input("Message d'Alice", "Bonjour Bob", key="a")
    
    if st.button("Lancer Essai A"):
        # Chiffrement AES-GCM
        cipher = AES.new(CLE_SECRETE, AES.MODE_GCM)
        ciphertext, tag = cipher.encrypt_and_digest(message_a.encode('utf-8'))
        nonce = cipher.nonce
        
        st.write("**Texte chiffré intercepté par Eve :**", ciphertext.hex())
        st.error("Eve ne peut pas lire le message sans la clé secrète.")
        
        # Déchiffrement par Bob avec la bonne clé
        cipher_bob = AES.new(CLE_SECRETE, AES.MODE_GCM, nonce=nonce)
        message_dechiffre = cipher_bob.decrypt_and_verify(ciphertext, tag).decode('utf-8')
        st.success(f"Bob a déchiffré le message : {message_dechiffre}")

# --- Essai B : Clé obtenue par Eve ---
with tab2:
    st.header("Essai B — Clé obtenue par Eve")
    message_b = st.text_input("Message d'Alice", "Données confidentielles", key="b")
    
    if st.button("Lancer Essai B"):
        cipher = AES.new(CLE_SECRETE, AES.MODE_GCM)
        ciphertext, tag = cipher.encrypt_and_digest(message_b.encode('utf-8'))
        nonce = cipher.nonce
        
        st.write("**Texte chiffré :**", ciphertext.hex())
        st.warning("Eve a réussi à obtenir la clé secrète.")
        
        # Eve déchiffre avec la clé compromise
        cipher_eve = AES.new(CLE_SECRETE, AES.MODE_GCM, nonce=nonce)
        message_eve = cipher_eve.decrypt_and_verify(ciphertext, tag).decode('utf-8')
        st.success(f"Eve lit le message en clair : {message_eve}")

# --- Essai C : Message modifié ---
with tab3:
    st.header("Essai C — Message modifié")
    message_c = st.text_input("Message d'Alice", "Envoyer 100 euros", key="c")
    
    if st.button("Lancer Essai C"):
        cipher = AES.new(CLE_SECRETE, AES.MODE_GCM)
        ciphertext, tag = cipher.encrypt_and_digest(message_c.encode('utf-8'))
        nonce = cipher.nonce
        
        # Eve modifie le texte chiffré en transit
        ciphertext_modifie = bytearray(ciphertext)
        ciphertext_modifie[0] ^= 0xFF # Modification d'un octet
        
        st.write("**Texte modifié par Eve :**", bytes(ciphertext_modifie).hex())
        
        # Bob essaie de déchiffrer le message altéré
        try:
            cipher_bob = AES.new(CLE_SECRETE, AES.MODE_GCM, nonce=nonce)
            cipher_bob.decrypt_and_verify(bytes(ciphertext_modifie), tag)
            st.success("Message accepté.")
        except Exception:
            st.error("Modification détectée ! Le message a été rejeté par AES-GCM.")
