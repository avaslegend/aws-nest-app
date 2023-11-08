module.exports = () => {
    return {
      defaultStage: 'dev',
      currentStage: '${opt:stage, self:custom.defaultStage}',
      managerStoreKeys: '/sava/avasapp/${opt:stage, self:provider.stage}/app_enviroment',
      'serverless-offline': {
        httpPort: 3003,
        lambdaPort: 3005
      }    
    };
  };