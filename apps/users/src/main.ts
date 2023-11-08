import { HttpStatus } from '@nestjs/common';
import { NestFactory } from '@nestjs/core';
import { Callback, Context, Handler } from 'aws-lambda';
import { AppModule } from './app.module';
import { AppService } from './app.service';

export const getUser: Handler = async (
  event: any,
  _context: Context,
  _callback: Callback,
) => {
  const appContext = await NestFactory.createApplicationContext(AppModule);
  const appService = appContext.get(AppService);
  const { id } = event.pathParameters;
  try {
    const res = await appService.getUser(id);
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

export const getUsers: Handler = async (
  _event: any,
  _context: Context,
  _callback: Callback,
) => {
  const appContext = await NestFactory.createApplicationContext(AppModule);
  const appService = appContext.get(AppService);
  try {
    const res = await appService.getUsers();
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