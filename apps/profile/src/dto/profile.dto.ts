import { IsNotEmpty, IsOptional, IsString, MinLength } from 'class-validator'

export class CreateProfileDTO {
    @IsString()
    @IsNotEmpty()
    @MinLength(3)
    title: string;

    @IsString()
    @IsOptional()
    description?: string;
}

// export class CreateProfileDTO {
//     title: string;
//     description: string;
// }