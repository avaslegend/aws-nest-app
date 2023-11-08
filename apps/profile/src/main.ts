// import { NestFactory } from '@nestjs/core';
// import { ProfileModule } from './profile.module';

// async function bootstrap() {
//   const app = await NestFactory.create(ProfileModule);
//   await app.listen(3000);
// }
// bootstrap();


import { HttpStatus } from '@nestjs/common';
import { NestFactory } from '@nestjs/core';
import { Callback, Context, Handler } from 'aws-lambda';
import { ProfileModule } from './profile.module';
import { ProfileService } from './profile.service';
import { CreateProfileDTO  } from './dto/profile.dto';
import { validateOrReject } from 'class-validator'
import { plainToClass } from 'class-transformer';
import { sendSQSMessage } from '../../util/aws-services';

const SQS_CATEGORY_QUEUE_URL = process?.env?.SQS_CATEGORY_QUEUE_URL;

export const getProfile: Handler = async (
  event: any,
  _context: Context,
  _callback: Callback,
) => {
  const appContext = await NestFactory.createApplicationContext(ProfileModule);
  const appService = appContext.get(ProfileService);
  const { id } = event.pathParameters;
  try {
    const dataSend = {
      code: 20,
      message: "sending category information"
    };

    console.log("SQS_CATEGORY_QUEUE_URL-value: ", SQS_CATEGORY_QUEUE_URL);
    await sendSQSMessage(SQS_CATEGORY_QUEUE_URL, dataSend);

    const res = await appService.getProfile(id);
    return {
      statusCode: HttpStatus.OK,
      body: JSON.stringify(res),
    };
  } catch (error) {
    console.log(error);
    return {
      statusCode: HttpStatus.BAD_REQUEST,
      body: JSON.stringify(error.response ?? error.message),
    };
  }
};

export const createProfile: Handler = async (
  _event: any,
  _context: Context,
  _callback: Callback,
) => {
  const appContext = await NestFactory.createApplicationContext(ProfileModule);
  const appService = appContext.get(ProfileService);
  try {
    const profile = JSON.parse(_event.body);

    console.log(`createProfile-body: `, profile);
 
    const createProfileDTO: CreateProfileDTO = plainToClass(CreateProfileDTO, profile);
    await validateOrReject(createProfileDTO);
    
    const res = await appService.createProfile(profile);
    return {
      statusCode: HttpStatus.OK,
      body: JSON.stringify(res),
    };
  } catch (error) {
    console.error("Error create profile: ", error);

    if (error && Array.isArray(error)){
      console.debug("Error ValidationError: ", error[0].constraints);
      
      if(error[0].constraints){
        console.debug("Message-profile: ", error[0]?.constraints);
        return {
          statusCode: HttpStatus.BAD_REQUEST,
          body: JSON.stringify({"code":"-1", "message":"Input validation error.", "constraints": error[0].constraints}),
        };
      }
    }
    return {
      statusCode: HttpStatus.BAD_REQUEST,
      body: JSON.stringify(error.response ?? error.message),
    };
  }
};