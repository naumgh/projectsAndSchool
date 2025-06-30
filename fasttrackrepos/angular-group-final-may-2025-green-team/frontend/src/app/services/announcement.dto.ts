import { BasicUserDto } from "./basic-user.dto";

export interface AnnouncementDto {
    id: number;
    date: number; // timestamp
    title: string;
    message: string;
    author: BasicUserDto;
}