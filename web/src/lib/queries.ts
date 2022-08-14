import { gql } from '@apollo/client/core';

export const GET_TASKS = gql`
    query {
      tasks {
        id
        name
        isDone
      }
    }
  `;