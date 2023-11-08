// import { NestFactory } from '@nestjs/core';
// import { CategoryModule } from './category.module';

// async function bootstrap() {
//   const app = await NestFactory.create(CategoryModule);
//   await app.listen(3000);
// }
// bootstrap();


import { NestFactory } from '@nestjs/core';
import { Callback, Context, Handler } from 'aws-lambda';
import { CategoryModule } from './category.module';
import { CategoryService } from './category.service';


export const getCategory: Handler = async (
  event: any,
  _context: Context,
  _callback: Callback,
) => {
  for (const record of event.Records) {
    console.debug('request-event: ', event);
    const appContext = await NestFactory.createApplicationContext(CategoryModule);
    const appService = appContext.get(CategoryService);

    try {
      console.debug('request-body: ', JSON.parse(record.body));
      console.debug('request_context: ', _context);
      console.debug('request_callback: ', _callback);
    } catch (error) {
      console.error("Category-process: ", error);
    }
  }
};
