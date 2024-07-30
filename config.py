from dotenv import load_dotenv
import os

load_dotenv()

API_ID = int(os.getenv("20199401"))
API_HASH = os.getenv("fef19c51f063e89361af487efe939095")
BOT_TOKEN = os.getenv("7380228773:AAGghvP-nmJ1xs4VVCiHe9QfCBGCE1D0RSY")
SESSION_NAME = os.getenv("BQE0N-kABl-wJbwYvxPwN5ISH4ezGBF8-VVH2cu783A8ckT1yZpmvTDfzMvIBiCr5_cUSQ923qsIQZTq3jZ7BcxENb9lnLVPnxL3CNQ4CKRdSO0IobG463JMl9_OHdyO2vf7WC1rDrM0hT7hUvTKiAhZVnOjwElDQdjhIXf4qxcu16vWuV-iNBJVuSJIna-XrfKjY6MSN6RQ0rfXV6XOjX1VipHaYNPGCq8UKDDAuVeRyn4zKhioNs6ZfTgRkc_lzhfnjS33vXwj2HQU1z6TtXxLN5l1nAs1gogkjGDX4zWAFtatTOdn8qXstuiZWYYG84IRwhN2dkJfzM0ExBt9oTboyYkmogAAAAG1un2tAA")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
