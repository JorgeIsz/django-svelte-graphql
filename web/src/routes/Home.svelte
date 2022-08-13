<script>
  import { query } from "svelte-apollo";
  import { gql } from '@apollo/client/core';


  // 2. Execute the GET_BOOKS GraphQL query using the Apollo client
  //    -> Returns a svelte store of promises that resolve as values come in
  const GET_TASKS = gql`
    query {
      tasks {
        id
        name
        isDone
      }
    }
  `;
  const tasks = query(GET_TASKS);

</script>

<h1>Home!</h1>
{#if $tasks.loading}
  Loading...
{:else if $tasks.error}
  Error: {$tasks.error.message}
{:else if $tasks.data}
<ul>
  {#each $tasks.data.tasks as task}
    <li>
      <input type="checkbox" checked={task.isDone}>
      {task.name}
    </li>
  {/each}
</ul>
{/if}