import React, { useState } from "react";
import { useForm, Controller } from "react-hook-form";
import { connect } from 'react-redux'
import { UPDATE_PROJECT, UPDATE_GOVERNANCE, UPDATE_CONTRACT_VALUE } from "../../../../graphql/mutations"
// import { updateAction } from './updateAction'
import { useMutation } from '@apollo/react-hooks'

import { updateAction } from '../../../../store/index'
import _ from "lodash";

import {
  Container,
  Wizard,
  Card,
  Nav,
  NavItem,
  NavLink,
  CardFooter,
  CardBody,
  Button,
  Row,
  Col,
  Table,
  Form,
  FormGroup,
  Input,
  InputGroup,
  InputGroupAddon,
  Label,
  DropdownToggle,
  DropdownMenu,
  DropdownItem,
  UncontrolledDropdown
} from "../../../../components";
import { func } from "prop-types";


export const QuestionInput = props => {
  const { qu, name } = props;
  const { final } = props;
  const { control, handleSubmit } = useForm();
  const [ updateProject, { projectData } ] = useMutation(UPDATE_PROJECT);
  const [ updateContractValue, { contractData } ] = useMutation(UPDATE_CONTRACT_VALUE);
  const [ updateGovernance, { governanceData } ] = useMutation(UPDATE_GOVERNANCE);
  const [value, setValue] = React.useState([]);

  function nextPreprocess() {
    props.saveState(props.index, { id: props.id, value });
    props.nextFn();
  }

  function previousPreprocess() {
    props.saveState(props.index, { id: props.id, value });
    props.prevFn();
  }


  // const onSubmitProduct = (table, data) => {
  //   switch(table) {
  //     case 'PROJECT':
  //       return updateProject({ variables: { input: projectData }} )
  //     case 'CONTRACT_VALUE':
  //       return updateContractValue({ variables: { input: contractData }})
  //     case 'GOVERNANCE':
  //       return updateGovernance({ variables: { input: governanceData }})
  //     default:
  //       return updateProject({ variables: { input: projectData }} )
  //   }
  //   console.log("table", table )
  //   // updateProject({ variables: { input: data }} )
  //   // console.log(data.value)
  //   // data.value = "";
  // }

  const onSubmitProduct = (projectData) => {
    updateProject({ variables: { input: projectData }} )
    // console.log(table)
  }

  return (
    <div>
      <CardBody
        style={{
          height: "20vh",
          marginLeft: "100px"
        }}
      >
        <h1>{qu}</h1>
      </CardBody>
      <CardBody
        style={{
          height: "20vh",
          marginLeft: "100px"
        }}
      >
        <Form onSubmit={handleSubmit(onSubmitProduct)}>
          <FormGroup>
            <Label style={{
                marginLeft: '18px'
            }}>Please Enter...</Label>
            <Col sm={3}>
            <Controller as={<Input />} type="number" name={name} control={control} defaultValue="" />              <input type="submit" />
            </Col>
          </FormGroup>
        </Form>
      </CardBody>
      <CardFooter className="p-4 bt-0">
        <div className="d-flex">
          <Button onClick={previousPreprocess} color="primary" className="mr-3">
            <i className="fa fa-angle-left mr-2"></i>
            Previous
          </Button>
          <Button
            onClick={nextPreprocess}
            color="primary"
            className="ml-auto px-4"
          >
            {final ? "Finish" : "Next"}
            <i className="fa fa-angle-right ml-2"></i>
          </Button>
        </div>
      </CardFooter>
    </div>
  );
};


// const mapStateToProps = (state) => {
//   return {
//     bodyObject: state.bodyObject
//   }
// }

// const mapDispatchToProps = { updateAction}

export default QuestionInput;

// connect(({ }) => ({  }), updateAction)(QuestionInput)

// export default connect(state => ({ data: updateAction(state) }))(QuestionInput)
// export default connect(mapStateToProps, mapDispatchToProps)(QuestionInput)



