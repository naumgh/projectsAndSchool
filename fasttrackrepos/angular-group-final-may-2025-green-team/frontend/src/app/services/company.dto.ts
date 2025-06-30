import { TeamDto } from "./team.service";
import { BasicUserDto } from "./basic-user.dto";

export interface CompanyDto {
    id: number;
    name: string;
    description: string;
    teams: TeamDto[];
    employees: BasicUserDto[];
}