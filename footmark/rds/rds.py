from footmark.rds.rdsobject import TaggedRDSObject

class Instance(TaggedRDSObject):
    def __init__(self, connection=None, owner_id=None,
                 name=None, description=None, id=None):
        super(Instance, self).__init__(connection)
        self.tags = {}

    def __repr__(self):
        return 'Instance:%s' % self.id

    def __getattr__(self, name):
        if name == 'id':
             return self.dbinstance_id

    def __setattr__(self, name, value):
        if name == 'id':
             self.dbinstance_id=value     
        super(TaggedRDSObject, self).__setattr__(name, value)
    
    def restart(self):
        '''
        restart
        '''
        return self.connection.restart_rds_instance(self.dbinstance_id)
    
    def terminate(self):
        '''
        terminate
        '''
        return self.connection.release_rds_instance(self.dbinstance_id)
    
    def release_public_connection_string(self, current_connection_string):
        '''
        release public connection string
        '''
        return self.connection.release_instance_public_connection_string(self.dbinstance_id, current_connection_string)
    
    def modify_specification(self, pay_type, db_instance_class=None, db_intance_storage=None):
        '''
        modify instance specification
        '''
        return self.connection.modify_instance_specification(self.dbinstance_id, pay_type, db_instance_class, db_intance_storage)
    
    def modify_billing_method(self, pay_type, period=None, used_time=None):
        '''
        modify instance billing method
        '''
        return self.connection.modify_instance_billing_method(self.dbinstance_id, pay_type, period, used_time)
    
    def modify_auto_renewal_attribute(self, auto_renew, duration):
        '''
        modify instance auto renewal attribute
        '''
        return self.connection.modify_instance_auto_renewal_attribute(self.dbinstance_id, auto_renew, duration)
    
    def allocate_public_connection_string(self, public_connection_string_prefix, port):
        '''
        allocate instance public connection string
        '''
        return self.connection.allocate_instance_public_connection_string(self.dbinstance_id, public_connection_string_prefix, port)
    
    def allocate_private_connection_string(self, private_connection_string_prefix, port=None):
        '''
        allocate instance private connection string
        '''
        return self.connection.allocate_instacne_private_connection_string(self.dbinstance_id, private_connection_string_prefix, port)
    
    def modify_connection_string(self, current_connection_string, connection_string_prefix=None, port=None):
        '''
        modify instance connection string
        '''
        return self.connection.modify_instance_connection_string(self.dbinstance_id, current_connection_string, connection_string_prefix, port)
    
class Account(TaggedRDSObject):
    def __init__(self, connection=None, owner_id=None,
                 name=None, description=None, id=None):
        super(Account, self).__init__(connection)
        self.tags = {}

    def __repr__(self):
        return 'Account:%s' % self.name

    def __getattr__(self, name):
        if name == 'name':
             return self.account_name
        if name == 'status':
             return self.account_status
        if name == 'description':
             return self.account_description
        if name == 'privileges':
             return self.database_privileges

    def __setattr__(self, name, value):
        if name == 'name':
             self.account_name=value
        if name == 'status':
             self.account_status=value
        if name == 'description':
             self.account_description=value
        if name == 'privileges':
             self.database_privileges=value
        super(TaggedRDSObject, self).__setattr__(name, value)
    
    def reset(self, dbinstance_id, account_password):
        '''
        reset
        '''
        return self.connection.reset_account_password(dbinstance_id, self.account_name, account_password)
    
    def grant_privilege(self, dbinstance_id, db_name, account_privilege):
        '''
        grant privilege
        '''
        return self.connection.grant_account_privilege(dbinstance_id, self.account_name, db_name, account_privilege)
    
    def revoke_privilege(self, dbinstance_id, db_name):
        '''
        revoke privilege
        '''
        return self.connection.revoke_account_privilege(dbinstance_id, self.account_name, db_name)
    
    def modify_description(self, dbinstance_id, description):
        '''
        modify description
        '''
        return self.connection.modify_account_description(dbinstance_id, self.account_name, description)
    
    def delete(self, dbinstance_id):
        '''
        delete account 
        '''
        return self.connection.delete_account(dbinstance_id, self.account_name)
