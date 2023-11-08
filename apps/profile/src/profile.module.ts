// import { Module } from '@nestjs/common';
// import { ProfileController } from './profile.controller';
// import { ProfileService } from './profile.service';

// @Module({
//   imports: [],
//   controllers: [ProfileController],
//   providers: [ProfileService],
// })
// export class ProfileModule {}

import { Module } from '@nestjs/common';
import { ProfileService } from './profile.service';

@Module({
  imports: [],
  providers: [ProfileService],
})
export class ProfileModule {}
