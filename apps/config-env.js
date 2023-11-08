module.exports = () =>  {
    return {
        DYNAMODB_TABLE: '${self:service}-${opt:stage, self:provider.stage}',
        MANAGER_STORE_KEYS: '${self:custom.managerStoreKeys}',
        GLOBAL_KEYS: '${ssm:${self:custom.managerStoreKeys}}'
    };
  };