<script>
  import { Router, Link, Route } from "svelte-routing";
  import Home from "./routes/Home.svelte";
  import About from "./routes/About.svelte";

  export let url = "";
  import {
    ApolloClient,
    InMemoryCache,
    createHttpLink,
  } from "@apollo/client/core";
  import { setContext } from '@apollo/client/link/context';
  import { setClient } from "svelte-apollo";

  const httpLink = createHttpLink({
    uri: "http://localhost:8000/graphql/",
  });
  const authLink = setContext((_, { headers }) => {
  const token = localStorage.getItem("token");
  return {
    headers: {
      ...headers,
      authorization: token ? `Bearer ${token}` : "",
    }
  }
});
  const client = new ApolloClient({
    link: authLink.concat(httpLink),
    cache: new InMemoryCache(),
  });
  setClient(client);
</script>

<Router {url}>
  <nav>
    <Link to="/">Home</Link>
    <Link to="about">About</Link>
  </nav>
  <div>
    <Route path="about" component={About} />
    <Route path="/"><Home /></Route>
  </div>
</Router>
