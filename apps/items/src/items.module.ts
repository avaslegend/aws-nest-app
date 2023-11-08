// import { Module } from '@nestjs/common';
// import { ItemsController } from './items.controller';
// import { ItemsService } from './items.service';

// @Module({
//   imports: [],
//   controllers: [ItemsController],
//   providers: [ItemsService],
// })
// export class ItemsModule {}
import { Module } from '@nestjs/common';
import { ItemsService } from './items.service';

@Module({
  imports: [],
  providers: [ItemsService],
})
export class ItemsModule {}
