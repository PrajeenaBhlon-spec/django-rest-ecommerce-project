async function refreshAccessToken() {
  const refresh = localStorage.getItem("refresh");

  if (!refresh) {
    return null;
  }

  const response = await fetch("/api/token/refresh/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ refresh }),
  });
  if (!response.ok) {
    return null;
  }
  const data = await response.json();
  localStorage.setItem("access", data.access);
  return data.access;
}

async function authFetch(url, options = {}) {
  let access = localStorage.getItem("access");
  options.headers = {
    ...options.headers,
    Authorization: `Bearer ${access}`
  };

  let response = await fetch(url, options);

  if (response.status === 401) {
    access = await refreshAccessToken();
    if (!access) return response;

    options.headers.Authorization = `Bearer ${access}`;
    response = await fetch(url, options);
  }
  return response;
}
