import { CredentialsDto } from "./credentials.dto";
import { ProfileDto } from "./profile.dto";

export interface UserRequestDto {
    credentials: CredentialsDto;
    profile: ProfileDto;
    admin: boolean;
}