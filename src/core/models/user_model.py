import dataclasses as dc

@dc.dataclass(unsafe_hash=True)
class UserModel:
    username: str
    password: str
    name: str
    email: str
    profile_image_url: str = None
    bio: str = None
