from pydantic import BaseModel


class SocialAccountCreate(BaseModel):
    platform_name: str
    profile_name: str


class SocialAccountResponse(BaseModel):
    id: int
    platform_name: str
    profile_name: str

    class Config:
        from_attributes = True