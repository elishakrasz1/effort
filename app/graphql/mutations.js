import React from 'react'
import gql from 'graphql-tag'

export const UPDATE_PROJECT = gql`
  mutation UpdateProject($input: ProjectUpdateMutationInput!) {
  updateProject(id: "8a97a516-cffe-4347-a481-b00dba325c30", input: $input) {
    ok
    output {
      id
      dbId
      projectName
    }
  }
}
`

export const UPDATE_CONTRACT_VALUE = gql`
    mutation UpdateContractValue($input: ContractvalueUpdateMutationInput!){
    updateContractValue(id: "b0764fd4-ffef-4352-ab2f-2df4003fc1e2", input: $input) {
      ok
      output {
        dbId
        id
        projectId
      }
    }
  }
`

export const UPDATE_GOVERNANCE = gql`
    mutation UpdateGovernance($input: ContractvalueUpdateMutationInput!) {
  updateGovernance(id: "6790fd64-c9b8-40cb-bbba-801d17a9b3a6", input: $input) {
    ok
    output {
      projectId
      dbId
      id
    }
  }
}
`

// {
//     "data": {
//       "createContractValue": {
//         "ok": true,
//         "output": {
//           "projectId": "8a97a516-cffe-4347-a481-b00dba325c30",
//           "dbId": "b0764fd4-ffef-4352-ab2f-2df4003fc1e2",
//           "id": "Q29udHJhY3R2YWx1ZU91dHB1dFR5cGU6YjA3NjRmZDQtZmZlZi00MzUyLWFiMmYtMmRmNDAwM2ZjMWUy"
//         }
//       }
//     }
//   }
