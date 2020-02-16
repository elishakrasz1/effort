import React, { useState } from "react";

import { useForm, Controller } from "react-hook-form";
import { connect } from 'react-redux'
import { updateAction } from '../../../../store/index'
import DatePicker from 'react-datepicker'
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
import { DatePickerComp } from "./DatePickerComp";
import { ButtonInput } from "../../../Forms/DatePicker/components";


const QuestionDate = props => {
  const { qu, name } = props;
  const { final } = props;
  const { control, handleSubmit, watch, reset } = useForm();
  const [data, setData] = useState(null)
  const [state, setStartDate] = useState()
  // const onSubmit = (data) => console.log(data)
  const onSubmit = (data) => props.updateAction(data)
  const [value, setValue] = React.useState("");

  function nextPreprocess() {
    props.saveState(props.index, { id: props.id, value });
    props.nextFn();
  }

  function previousPreprocess() {
    props.saveState(props.index, { id: props.id, value });
    props.prevFn();
  }

  // function onValueChange(newValue) {
  //   if (value === newValue) {
  //     setValue(newValue);
  //     return;
  //   }
  //   setValue(newValue);
  //   console.log('date', newValue)
  // }

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
          {/* <DatePickerComp 
            onClick={onValueChange}
            onValueChange={onValueChange}
          /> */}
          <Form  onSubmit={handleSubmit(onSubmit)}>
          {/* <Controller
                            as={
                                <DatePicker />
                            }
                            control={control}
                            rules={{ required: true }}
                            name="receivedDate"
                            label="Received Date"
                            value={watch('receivedDate')}
                            defaultValue={watch('receivedDate')}
                            onChange={date => {
                                setValue('receivedDate', date);
                                handleBlur(getValues().id, 'receivedDate'); //Managing patch save at server
                                return {value: date} //important to update the controller value after change else state is updated and the controller will not render
                            }}
                            disabled={state.disabled}
                            format="dd/MM/yyyy" //This will cause the value of received date to have an ISO date and a formatted date in an array, so it's recommended you use watch(name)[0] to extract the ISO date and [1] for the formatted date.
                            autoOk
                            margin="normal"
                        /> */}
                        <Controller
                            as={
                                <DatePicker />
                            }
                            control={control}
                            rules={{ required: true }}
                            name={name}
                            label={name}
                            value={watch(`${name}`)}
                            defaultValue={watch(`${name}`)}
                            onChange={date => {
                                setValue(`${name}`, date);
                                // handleBlur(getValues().id, `${name}`); //Managing patch save at server
                                return {value: date} //important to update the controller value after change else state is updated and the controller will not render
                            }}
                            // disabled={state.disabled}
                            name={name}
                            control={control}
                            format="dd/MM/yyyy" //This will cause the value of received date to have an ISO date and a formatted date in an array, so it's recommended you use watch(name)[0] to extract the ISO date and [1] for the formatted date.
                            autoOk
                            margin="normal"
                        />
                        {/* <Controller 
                          style={{
                            width: '100px'
                          }}
                          as={
                            <DatePicker
                              customInput={<ButtonInput />}
                              showTimeSelect
                              name={name}
                              timeFormat="hh:mm aa"
                              timeIntervals={30}
                              timeCaption="time"
                              dateFormat="MMMM Do, yyyy hh:mm aa"
                              rules={{ required: true }}
                              onChange={date => setStartDate(date)}
                            />
                          }
                          name={name}
                          control={control}
                        /> */}
                        <input type="submit" />
          </Form>
        
          
        {/* <Form>
          <FormGroup>
            <Label for="exampleEmail">Please Enter...Date</Label>
            <Col sm={3}>
              <Input
                type="number"
                name=""
                placeholder="USD"
                onChange={onValueChange}
                value={value}
              />
            </Col>
          </FormGroup>
        </Form> */}
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

const mapStateToProps = (state) => {
  return {
    bodyObject: state.bodyObject
  }
}

const mapDispatchToProps = { updateAction}

export default connect(mapStateToProps, mapDispatchToProps)(QuestionDate)

// export default QuestionDate;
