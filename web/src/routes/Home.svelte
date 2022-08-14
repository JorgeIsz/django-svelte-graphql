<script lang="ts">
  import { query } from "svelte-apollo";
  import { GET_TASKS } from "@/lib/queries";

  
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