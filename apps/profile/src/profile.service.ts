// import { Injectable } from '@nestjs/common';

// @Injectable()
// export class ProfileService {
//   getHello(): string {
//     return 'Hello World!';
//   }
// }

import { Injectable, InternalServerErrorException } from '@nestjs/common';
import { v1 } from 'uuid';
//const { v4: uuidv4 } = require('uuid');

import { DynamoDB } from 'aws-sdk';

const db = new DynamoDB.DocumentClient();

@Injectable()
export class ProfileService {
  async createProfile(item: any) {
    const { title, description } = item;
    const createdOn = new Date().getTime();

    const data = {
      TableName: process.env.DYNAMODB_TABLE,
      Item: {
        id: v1(),
        title,
        description,
        createdOn,
      },
    };

    try {
      await db.put(data).promise();
      return item;
    } catch (error) {
      throw new InternalServerErrorException(error.message);
    }
  }

  async getProfile(id: string) {
    const params = {
      TableName: process.env.DYNAMODB_TABLE,
      Key: { id },
    };

    try {
      const result = await db.get(params).promise();
      return result.Item;
    } catch (error) {
      throw new InternalServerErrorException(error.message);
    }
  }

}