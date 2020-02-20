# Imports
import datetime
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID
from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()
# metadata = Base.metadata

from flask_graphql import GraphQLView
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import os

basedir = os.path.abspath(os.path.dirname(__file__))
# app initialization
app = Flask(__name__)
CORS(app)
app.debug = True
# Configs
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Password1@localhost/rachel'
SQLALCHEMY_TRACK_MODIFICATIONS = True
db = SQLAlchemy(app)

# TO-DO
# Modules
db = SQLAlchemy(app)
# TO-DO
# Models

# class User(db.Model):
#     __tablename__ = 'user'

#     id = db.Column(UUID, primary_key=True)
#     username = db.Column(db.String(255))
#     email = db.Column(db.String(255))
#     phone = db.Column(db.String(16))
#     ccode = db.Column(db.String(8))

#     def __repr__(self):
#         return '<User %r>' % self.username


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(16))
    ccode = db.Column(db.String(8))
    CREATED_BY = db.Column(db.Integer)
    UPDATED_BY = db.Column(db.Integer)
    UPDATED_AT = db.Column(db.DateTime, server_default=db.func.now())
    CREATED_AT = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return '<User %r>' % self.username


class UserProject(db.Model):
    __tablename__ = 'user_project'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('user.id'))
    project_id = db.Column(db.ForeignKey('project.id'))
    CREATED_BY = db.Column(db.Integer)
    UPDATED_BY = db.Column(db.Integer)
    UPDATED_AT = db.Column(db.DateTime, server_default=db.func.now())
    CREATED_AT = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    project = relationship('Project')
    user = relationship('User')

    def __repr__(self):
        return '<UserProject %r>' % self.project_id

class Project(db.Model):
    __tablename__ = 'project'

    id = db.Column(db.Integer, primary_key=True)
    c_project_id = db.Column(db.String(255))
    project_name = db.Column(db.String(255))
    signature_date = db.Column(db.DateTime(255))
    service_commencement = db.Column(db.DateTime(255))
    contract_duration_month = db.Column(db.Integer)
    contract_value_usd = db.Column('contract value_usd', db.Numeric)
    projected_margin = db.Column(db.Numeric)
    component_of_bespoke = db.Column(db.Integer)
    often_provide_services = db.Column(db.Integer)
    is_transition_plan = db.Column(db.Integer)
    transition_plan_date = db.Column(db.DateTime(255))
    is_transition_charges = db.Column(db.Integer)
    transition_charges = db.Column(db.Numeric)
    milestones = db.Column(db.Integer)
    payment_milestones = db.Column(db.Integer)
    service_credit_cap = db.Column(db.Integer)
    is_transformation_plan = db.Column(db.Integer)
    transformation_plan_start = db.Column(db.DateTime(255))
    transformation_plan_end = db.Column(db.DateTime(255))
    is_earn_back = db.Column(db.Integer)
    is_customer_satisfaction_report = db.Column(db.Integer)
    customer_satisfaction_form = db.Column(db.Integer)
    governance_type = db.Column(db.Integer)
    governance_often = db.Column(db.Integer)
    key_personnel = db.Column(db.Integer)
    supplier_personnel = db.Column(db.Integer)
    customer_personnel = db.Column(db.Integer)
    planned_negotiation_month = db.Column(db.Integer)
    negotiations_month = db.Column(db.Integer)
    sole_sourced = db.Column(db.Integer)
    proposed_period_weeks = db.Column(db.Integer)
    actual_period_weeks = db.Column(db.Integer)
    is_due_diligence_completed = db.Column(db.Integer)
    agreement_party = db.Column('agreement party', db.Integer)
    type_of_service = db.Column(db.Integer)
    currency = db.Column(db.Integer)
    service_credit_cap_type = db.Column(db.Integer)
    service_level_without_credit = db.Column(db.Integer)
    service_levels_with_credit = db.Column(db.Integer)
    service_level_cap_percentage = db.Column(db.Numeric)
    CREATED_BY = db.Column(UUID)
    UPDATED_BY = db.Column(UUID)
    UPDATED_AT = db.Column(db.DateTime, server_default=db.func.now())
    CREATED_AT = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    
    def __repr__(self):
        return '<Project %r>' % self.project_name

class Bespoke(db.Model):
    __tablename__ = 'bespoke'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer)
    project_id = db.Column(db.ForeignKey('project.id'))
    CREATED_BY = db.Column(db.Integer)
    UPDATED_BY = db.Column(db.Integer)
    UPDATED_AT = db.Column(db.DateTime, server_default=db.func.now())
    CREATED_AT = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    project = relationship('Project')
    
    def __repr__(self):
        return '<Bespoke %r>' % self.bespoke
     
class ContractValue(db.Model):
    __tablename__ = 'contract_value'

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    contract_value_usd = db.Column(db.Numeric)
    project_id = db.Column(ForeignKey('project.id'))
    estimated_cost_usd = db.Column(db.Numeric)
    CREATED_BY = db.Column(db.Integer)
    UPDATED_BY = db.Column(db.Integer)
    UPDATED_AT = db.Column(db.DateTime, server_default=db.func.now())
    CREATED_AT = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    project = relationship('Project')
    
    def __repr__(self):
        return '<ContractValue %r>' % self.project_id

class Milestone(db.Model):
    __tablename__ = 'milestone'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer)
    project_id = db.Column(db.ForeignKey('project.id'))
    is_payment = db.Column(db.Integer)
    completion_date = db.Column(db.DateTime(255))
    charges = db.Column(db.Numeric)
    is_paied = db.Column(db.ForeignKey('questionnaire.id'))
    CREATED_BY = db.Column(db.Integer)
    UPDATED_BY = db.Column(db.Integer)
    UPDATED_AT = db.Column(db.DateTime, server_default=db.func.now())
    CREATED_AT = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())


    questionnaire = relationship('Questionnaire')
    project = relationship('Project')
    
    def __repr__(self):
        return '<Milestone %r>' % self.milestone

class Questionnaire(db.Model):
    __tablename__ = 'questionnaire'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.ForeignKey('project.id'))
    user_filler = db.Column(db.ForeignKey('user.id'))
    to_date = db.Column(db.DateTime(255))
    is_transition_completed = db.Column(db.Integer)
    is_transition_charges_paied = db.Column(db.Integer)
    is_transformation_completed = db.Column(db.Integer)
    missed_kpi = db.Column(db.Integer)
    missed_service_level = db.Column(db.Integer)
    moved_service_level = db.Column(db.Integer)
    payable_service_credits = db.Column(db.Integer)
    paied_service_credits = db.Column(db.Integer)
    is_paied_passed = db.Column(db.Integer)
    pay_back = db.Column(db.Numeric)
    is_customer_satisfaction_report = db.Column(db.Integer)
    customer_satisfaction_result = db.Column(db.Integer)
    is_governance = db.Column(db.Integer)
    is_governance_minute = db.Column(db.Integer)
    is_additional_governance = db.Column(db.Integer)
    additional_governance_cause = db.Column(db.Integer)
    is_formal_notices = db.Column(db.Integer)
    formal_notices_about = db.Column(db.Integer)
    formal_notices_type = db.Column(db.Integer)
    initiated_CCNs = db.Column(db.Integer)
    signed_CCNs = db.Column(db.Integer)
    signed_CCNs_type = db.Column(db.Integer)
    key_personnel_changed = db.Column(db.Integer)
    supplier_personnel_changed = db.Column(db.Integer)
    customer_personnel_changed = db.Column(db.Integer)
    invoiced_charges_usd = db.Column(db.Numeric)
    is_not_invoiced = db.Column(db.Integer)
    CREATED_BY = db.Column(UUID)
    UPDATED_BY = db.Column(UUID)
    UPDATED_AT = db.Column(db.DateTime, server_default=db.func.now())
    CREATED_AT = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    project = relationship('Project')
    user = relationship('User')
    
def __repr__(self):
        return '<Questionnaire %r>' % self.project_id


class UserObject(SQLAlchemyObjectType):
   class Meta:
       model = User
       interfaces = (graphene.relay.Node, )

class UserProjectObject(SQLAlchemyObjectType):
   class Meta:
       model = UserProject
       interfaces = (graphene.relay.Node, )
       
class ProjectObject(SQLAlchemyObjectType):
   class Meta:
       model = Project
       interfaces = (graphene.relay.Node, )
       
class BespokeObject(SQLAlchemyObjectType):
   class Meta:
       model = Bespoke
       interfaces = (graphene.relay.Node, )

class MilestoneObject(SQLAlchemyObjectType):
   class Meta:
       model = Milestone
       interfaces = (graphene.relay.Node, )

class ContractValueObject(SQLAlchemyObjectType):
   class Meta:
       model = ContractValue
       interfaces = (graphene.relay.Node, )      
       
class QuestionnaireObject(SQLAlchemyObjectType):
   class Meta:
       model = Questionnaire
       interfaces = (graphene.relay.Node, )
       
class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_users = SQLAlchemyConnectionField(UserObject)
    all_projects = SQLAlchemyConnectionField(ProjectObject)
    all_bespoke = SQLAlchemyConnectionField(BespokeObject)
    all_contract_values = SQLAlchemyConnectionField(ContractValueObject)
    all_questionnaires = SQLAlchemyConnectionField(QuestionnaireObject)
    all_milestones = SQLAlchemyConnectionField(MilestoneObject)
    all_user_projects = SQLAlchemyConnectionField(UserProjectObject)

class UserInput(graphene.InputObjectType):
    username = graphene.String()
    email = graphene.String()
    phone = graphene.String()
    ccode = graphene.String()

class CreateUser(graphene.Mutation):
    class Arguments:
        user_data = UserInput()
 
    ok = graphene.Boolean()
    user = graphene.Field(UserObject)

    def mutate(root,info, user_data=None):
        user = User(
            username=user_data.username, email=user_data.email, phone=user_data.phone, ccode=user_data.ccode
        )

        db.session.add(user)
        db.session.commit()   
        ok = True
        return CreateUser(user=user, ok=ok)

class UpdateUserInput(graphene.InputObjectType):
# class UpdateUserInput(graphene.InputObjectType, UserInput):
    id = graphene.ID(required = True)
    
class UpdateUser(graphene.Mutation):
    class Arguments:
        user_data = UpdateUserInput()

    ok = graphene.Boolean()
    user = graphene.Field(UserObject)
    
    def mutate(root,info, user_data=None):
        user = User(
            username=user_data.username, email=user_data.email, phone=user_data.phone, ccode=user_data.ccode
        )

        db.session.update(user)
        db.session.commit()   
        ok = True
        return UpdateUser(user=user, ok=ok)

class QuestionnaireInput(graphene.InputObjectType): 
    project_id = graphene.Int()
    user_filler = graphene.Int()
    to_date = graphene.types.datetime.DateTime()
    is_transition_completed = graphene.Int()
    is_transition_charges_paied = graphene.Int()
    is_transformation_completed = graphene.Int()
    missed_kpi = graphene.Int()
    missed_service_level = graphene.Int()
    moved_service_level = graphene.Int()
    payable_service_credits = graphene.Int()
    paied_service_credits = graphene.Int()
    is_paied_passed = graphene.Int()
    pay_back = graphene.Float()
    is_customer_satisfaction_report = graphene.Int()
    customer_satisfaction_result = graphene.Int()
    is_governance = graphene.Int()
    is_governance_minute = graphene.Int()
    is_additional_governance = graphene.Int()
    additional_governance_cause = graphene.Int()
    is_formal_notices = graphene.Int()
    formal_notices_about = graphene.Int()
    formal_notices_type = graphene.Int()
    initiated_CCNs = graphene.Int()
    signed_CCNs = graphene.Int()
    signed_CCNs_type = graphene.Int()
    key_personnel_changed = graphene.Int()
    supplier_personnel_changed = graphene.Int()
    customer_personnel_changed = graphene.Int()
    invoiced_charges_usd = graphene.Float()
    is_not_invoiced = graphene.Int()
    
class CreateQuestionnaire(graphene.Mutation):
    class Arguments:

        questionnaire_data = QuestionnaireInput()
 
    ok = graphene.Boolean()
    questionnaire = graphene.Field(QuestionnaireObject)

    def mutate(root,info, questionnaire_data=None):
        questionnaire = Questionnaire(
                project_id = questionnaire_data.project_id,
    user_filler = questionnaire_data.user_filler,
    to_date = questionnaire_data.to_date,
    is_transition_completed = questionnaire_data.is_transformation_completed,
    is_transition_charges_paied = questionnaire_data.is_transition_charges_paied,
    is_transformation_completed = questionnaire_data.is_transformation_completed,
    missed_kpi = questionnaire_data.missed_kpi,
    missed_service_level = questionnaire_data.missed_service_level,
    moved_service_level = questionnaire_data.moved_service_level,
    payable_service_credits = questionnaire_data.payable_service_credits,
    paied_service_credits = questionnaire_data.paied_service_credits,
    is_paied_passed = questionnaire_data.is_paied_passed,
    pay_back = grquestionnaire_data.pay_back,
    is_customer_satisfaction_report = questionnaire_data.is_customer_satisfaction_report,
    customer_satisfaction_result = questionnaire_data.customer_satisfaction_result,
    is_governance = questionnaire_data.is_governance,
    is_governance_minute = questionnaire_data.is_governance_minute,
    is_additional_governance = questionnaire_data.is_additional_governance,
    additional_governance_cause = questionnaire_data.additional_governance_cause,
    is_formal_notices = questionnaire_data.is_formal_notices,
    formal_notices_about = questionnaire_data.formal_notices_about,
    formal_notices_type = questionnaire_data.formal_notices_type,
    initiated_CCNs = questionnaire_data.initiated_CCNs,
    signed_CCNs = questionnaire_data.signed_CCNs,
    signed_CCNs_type = questionnaire_data.signed_CCNs_type,
    key_personnel_changed = questionnaire_data.key_personnel_changed,
    supplier_personnel_changed = questionnaire_data.supplier_personnel_changed,
    customer_personnel_changed = questionnaire_data.customer_personnel_changed,
    invoiced_charges_usd = grquestionnaire_data.invoiced_charges_usd,
    is_not_invoiced = questionnaire_data.is_not_invoiced
        )
        db.session.add(questionnaire)
        db.session.commit()   
        ok = True
        return CreateProject(questionnaire=questionnaire, ok=ok)
    
class ProjectInput(graphene.InputObjectType):
    c_project_id = graphene.String()
    project_name = graphene.String()
    signature_date = graphene.types.datetime.DateTime()
    service_commencement = graphene.types.datetime.DateTime()
    contract_duration_month = graphene.Int()
    contract_value_usd = graphene.Float()
    projected_margin = graphene.Float()
    component_of_bespoke = graphene.Int()
    often_provide_services = graphene.Int()
    is_transition_plan = graphene.Int()
    transition_plan_date = graphene.types.datetime.DateTime()
    is_transition_charges = graphene.Int()
    transition_charges = graphene.Float()
    is_transformation_plan = graphene.Int()
    transformation_plan_start = graphene.types.datetime.DateTime()
    transformation_plan_end = graphene.types.datetime.DateTime()
    service_credit_cap = graphene.Int()
    is_earn_back = graphene.Int()
    is_customer_satisfaction_report = graphene.Int()
    customer_satisfaction_form = graphene.Int()
    governance_type = graphene.Int()
    governance_often = graphene.Int()
    key_personnel = graphene.Int()
    supplier_personnel = graphene.Int()
    customer_personnel = graphene.Int()
    planned_negotiation_month = graphene.Int()
    negotiations_month = graphene.Int()
    sole_sourced = graphene.Int()
    proposed_period_weeks = graphene.Int()
    actual_period_weeks = graphene.Int()
    is_due_diligence_completed = graphene.Int()
    agreement_party = graphene.Int()
    type_of_service = graphene.Int()
    currency = graphene.Int()
    service_levels_with_credit = graphene.Int()
    service_level_without_credit = graphene.Int()
    service_level_cap_percentage = graphene.Int()
    service_credit_cap_type = graphene.Int()

class CreateProject(graphene.Mutation):
    class Arguments:

        project_data = ProjectInput()

    ok = graphene.Boolean()
    project = graphene.Field(ProjectObject)

    def mutate(root, info, project_data=None):
        project = Project(
            c_project_id=project_data.c_project_id, project_name = project_data.project_name, signature_date=project_data.signature_date, service_commencement=project_data.service_commencement, contract_duration_month=project_data.contract_duration_month, contract_value_usd=project_data.contract_value_usd, projected_margin=project_data.projected_margin, often_provide_services=project_data.often_provide_services, is_transition_plan=project_data.is_transition_plan,
            transition_plan_date=project_data.transition_plan_date,
            is_transition_charges=project_data.is_transition_charges,
            transition_charges=project_data.transition_charges, is_transformation_plan=project_data.is_transformation_plan, transformation_plan_start=project_data.transformation_plan_start, transformation_plan_end=project_data.transformation_plan_end, is_earn_back=project_data.is_earn_back, is_customer_satisfaction_report=project_data.is_customer_satisfaction_report, service_level_without_credit=project_data.service_level_without_credit, service_levels_with_credit=project_data.service_levels_with_credit, service_credit_cap_type=project_data.service_credit_cap_type, customer_satisfaction_form=project_data.customer_satisfaction_form, governance_type=project_data.governance_type, governance_often=project_data.governance_often, key_personnel=project_data.key_personnel, supplier_personnel=project_data.supplier_personnel, customer_personnel=project_data.customer_personnel, planned_negotiation_month=project_data.planned_negotiation_month, negotiations_month=project_data.negotiations_month, sole_sourced=project_data.sole_sourced, proposed_period_weeks=project_data.proposed_period_weeks, actual_period_weeks=project_data.actual_period_weeks, is_due_diligence_completed=project_data.is_due_diligence_completed, agreement_party = project_data.agreement_party, type_of_service = project_data.type_of_service, currency = project_data.currency, service_level_cap_percentage = project_data.service_level_cap_percentage
        )
        db.session.add(project)
        db.session.commit()
        ok = True
        return CreateProject(project=project, ok=ok)

class UpdateProjectInput(graphene.InputObjectType):
    id = graphene.Int(required = True)
    c_project_id = graphene.String()
    project_name = graphene.String()
    signature_date = graphene.types.datetime.DateTime()
    service_commencement = graphene.types.datetime.DateTime()
    contract_duration_month = graphene.Int()
    contract_value_usd = graphene.Float()
    projected_margin = graphene.Float()
    component_of_bespoke = graphene.Int()
    often_provide_services = graphene.Int()
    is_transition_plan = graphene.Int()
    transition_plan_date = graphene.types.datetime.DateTime()
    is_transition_charges = graphene.Int()
    transition_charges = graphene.Float()
    is_transformation_plan = graphene.Int()
    transformation_plan_start = graphene.types.datetime.DateTime()
    transformation_plan_end = graphene.types.datetime.DateTime()
    service_credit_cap = graphene.Int()
    is_earn_back = graphene.Int()
    is_customer_satisfaction_report = graphene.Int()
    customer_satisfaction_form = graphene.Int()
    governance_type = graphene.Int()
    governance_often = graphene.Int()
    key_personnel = graphene.Int()
    supplier_personnel = graphene.Int()
    customer_personnel = graphene.Int()
    planned_negotiation_month = graphene.Int()
    negotiations_month = graphene.Int()
    sole_sourced = graphene.Int()
    proposed_period_weeks = graphene.Int()
    actual_period_weeks = graphene.Int()
    is_due_diligence_completed = graphene.Int()
    agreement_party = graphene.Int()
    type_of_service = graphene.Int()
    currency = graphene.Int()
    service_levels_with_credit = graphene.Int()
    service_level_without_credit = graphene.Int()
    service_level_cap_percentage = graphene.Int()
    service_credit_cap_type = graphene.Int()

    
class UpdateProject(graphene.Mutation):
    class Arguments:

        project_data = UpdateProjectInput()

    ok = graphene.Boolean()
    project = graphene.Field(ProjectObject)
    
    @staticmethod
    def mutate(root, info, project_data=None):
       
        query = Project.get_query(info)
        project = query.filter(Project.id == 1)
        project = Project(
            id=project_data.id, c_project_id=project_data.c_project_id, project_name = project_data.project_name, signature_date=project_data.signature_date, service_commencement=project_data.service_commencement, contract_duration_month=project_data.contract_duration_month, contract_value_usd=project_data.contract_value_usd, projected_margin=project_data.projected_margin, often_provide_services=project_data.often_provide_services, is_transition_plan=project_data.is_transition_plan,
            transition_plan_date=project_data.transition_plan_date,
            is_transition_charges=project_data.is_transition_charges,
            transition_charges=project_data.transition_charges, is_transformation_plan=project_data.is_transformation_plan, transformation_plan_start=project_data.transformation_plan_start, transformation_plan_end=project_data.transformation_plan_end, is_earn_back=project_data.is_earn_back, is_customer_satisfaction_report=project_data.is_customer_satisfaction_report, service_levels_with_credit=project_data.service_levels_with_credit, service_level_without_credit=project_data.service_level_without_credit, service_credit_cap_type=project_data.service_credit_cap_type, customer_satisfaction_form=project_data.customer_satisfaction_form, governance_type=project_data.governance_type, governance_often=project_data.governance_often, key_personnel=project_data.key_personnel, supplier_personnel=project_data.supplier_personnel, customer_personnel=project_data.customer_personnel, planned_negotiation_month=project_data.planned_negotiation_month, negotiations_month=project_data.negotiations_month, sole_sourced=project_data.sole_sourced, proposed_period_weeks=project_data.proposed_period_weeks, actual_period_weeks=project_data.actual_period_weeks, is_due_diligence_completed=project_data.is_due_diligence_completed, agreement_party = project_data.agreement_party, type_of_service = project_data.type_of_service, currency = project_data.currency, service_level_cap_percentage = project_data.service_level_cap_percentage
        )
        # db.session.update(project)
        db.session.commit()
        ok = True

        return UpdateProject(project=project, ok=ok)

class BespokeInput(graphene.InputObjectType):
    type = graphene.String()
    project_id = graphene.Int()

class CreateBespoke(graphene.Mutation):
    class Arguments:
    
        bespoke_data = BespokeInput()
 
    ok = graphene.Boolean()
    bespoke = graphene.Field(BespokeObject)

    def mutate(root,info, bespoke_data=None):
        bespoke = Bespoke(
            type = bespoke_data.type, project_id = bespoke_data.project_id
        )

        db.session.add(bespoke)
        db.session.commit()   
        ok = True
        return CreateBespoke(bespoke=bespoke, ok=ok)

class UpdateBespokeInput(graphene.InputObjectType):
    id = graphene.ID(required = True)
    
class UpdateBespoke(graphene.Mutation):
    class Arguments:
        bespoke_data = UpdateBespokeInput()

    ok = graphene.Boolean()
    bespoke = graphene.Field(BespokeObject)
    
    def mutate(root,info, bespoke_data=None):
        bespoke = Bespoke(
            type = bespoke_data.type, project_id = bespoke_data.project_id
        )

        db.session.add(bespoke)
        db.session.commit()   
        ok = True
        return UpdateBespoke(bespoke=bespoke, ok=ok)

class MilestoneInput(graphene.InputObjectType):
    type = graphene.Int()
    is_payment = graphene.Int()
    completion_date = graphene.types.datetime.DateTime()
    project_id = graphene.Int()
    charges = graphene.Float()
    is_paied = graphene.Int()

class CreateMilestone(graphene.Mutation):
    class Arguments:
    
        milestone_data = MilestoneInput()
 
    ok = graphene.Boolean()
    milestone_data = graphene.Field(MilestoneObject)

    def mutate(root,info, milestone_data=None):
        milestone = Milestone(
            type = milestone_data.type, is_payment = milestone_data.is_payment, completion_date = milestone_data.completion_date, project_id = milestone_data.project_id, charges = milestone_data.charges, is_paied = milestone_data.is_paied
        )

        db.session.add(milestone)
        db.session.commit()   
        ok = True
        return Milestone(milestone=milestone, ok=ok)

class UpdateMilestoneInput(graphene.InputObjectType):
    id = graphene.ID(required = True)
    
class UpdateMilestone(graphene.Mutation):
    class Arguments:
        milestone_data = UpdateMilestoneInput()

    ok = graphene.Boolean()
    milestone = graphene.Field(MilestoneObject)
    
    def mutate(root,info, milestone_data=None):
        milestone = Milestone(
            type = milestone_data.type, is_payment = milestone_data.is_payment, completion_date = milestone_data.completion_date, project_id = milestone_data.project_id, charges = milestone_data.charges, is_paied = milestone_data.is_paied
        )

        db.session.update(milestone)
        db.session.commit()   
        ok = True
        return UpdateMilestone(milestone=milestone, ok=ok)

class ContractValueInput(graphene.InputObjectType):
    year = graphene.Int()
    contract_value_usd = graphene.Float()
    project_id = graphene.Int()
    estimated_cost_usd = graphene.Float()

class CreateContractValue(graphene.Mutation):
    class Arguments:
    
        contract_value_data = ContractValueInput()
 
    ok = graphene.Boolean()
    contract_value_data = graphene.Field(ContractValueObject)

    def mutate(root,info, contract_value_data=None):
        contract_value = ContractValue(
            year = contract_value_data.year, contract_value_usd = contract_value_data.contract_value_usd, project_id = contract_value_data.project_id, estimated_cost_usd = contract_value_data.estimated_cost_usd
        )

        db.session.add(contract_value)
        db.session.commit()   
        ok = True
        return CreateContractValue(contract_value=contract_value, ok=ok)

class UpdateContractValueInput(graphene.InputObjectType):
    id = graphene.ID(required = True)
    
class UpdateContractValue(graphene.Mutation):
    class Arguments:
        contract_value_data = UpdateContractValueInput()

    ok = graphene.Boolean()
    contract_value = graphene.Field(ContractValueObject)
    
    def mutate(root,info, contract_value_data=None):
        contract_value = ContractValue(
            year = contract_value_data.year, contract_value_usd = contract_value_data.contract_value_usd, project_id = contract_value_data.project_id, estimated_cost_usd = contract_value_data.estimated_cost_usd
        )

        db.session.update(contract_value)
        db.session.commit()   
        ok = True
        return UpdateContractValue(contract_value=contract_value, ok=ok)



         
class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_project = CreateProject.Field()
    create_questionnaire = CreateQuestionnaire.Field()
    create_bespoke = CreateBespoke.Field()
    create_milestone = CreateMilestone.Field()
    create_contract_value = CreateContractValue.Field()
    update_project = UpdateProject.Field()
    update_contract_value = UpdateContractValue.Field()
    update_user = UpdateUser.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)

# TO-DO
# Routes
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

# TO-DO
@app.route('/')
def index():
    return '<p> Hello World</p>'
if __name__ == '__main__':
     app.run()
