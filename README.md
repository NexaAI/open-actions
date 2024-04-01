# Open Actions
Welcome to our vibrant Open Actions Repo! 🌟 Here, we present an extensive collection of APIs that offer developers and AI enthusiatists seamless, free, and open-source integration options with the forefront of Large Language Model innovation.

Our Actions can integrate with the most influential names (but are not limited to) in the LLM area : OpenAI, Anthropic, Mixtral, Cohere, LangChain, LLamaIndex, etc.

<!-- Header -->
<h1 align="center">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="data/Octopus-logo.jpeg">
        <source media="(prefers-color-scheme: light)" srcset="data/Octopus-logo.jpeg">
        <img alt="Repository header" src="data/Octopus-logo.jpeg" height="55">
    </picture>
</h1>

<!-- Badges -->
<h4 align="center">
    <a href="https://github.com/NexaAI/open-actions/stargazers">
        <img alt="GitHub stars" src="https://img.shields.io/github/stars/bapo2/gpt-actions?style=flat-square&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48c3ZnIHdpZHRoPSIzNnB4IiBoZWlnaHQ9IjM2cHgiIHZpZXdCb3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNvbG9yPSIjZmZmZmZmIj48ZyBjbGlwLXBhdGg9InVybCgjY2xpcDBfMzA1N18xNDYyOCkiPjxwYXRoIGQ9Ik05Ljk1MjQyIDkuNjIyNzJMMTEuNTEwOSA2LjMxODE2QzExLjcxMSA1Ljg5Mzk1IDEyLjI4OSA1Ljg5Mzk1IDEyLjQ4OTEgNi4zMTgxNkwxNC4wNDc2IDkuNjIyNzJMMTcuNTMyOSAxMC4xNTU5QzE3Ljk4MDEgMTAuMjI0MyAxOC4xNTgzIDEwLjc5OTYgMTcuODM0NiAxMS4xMjk2TDE1LjMxMyAxMy43MDAxTDE1LjkwODEgMTcuMzMxNEMxNS45ODQ1IDE3Ljc5NzggMTUuNTE2OCAxOC4xNTM0IDE1LjExNjcgMTcuOTMzMUwxMiAxNi4yMTc3TDguODgzMjggMTcuOTMzMUM4LjQ4MzE2IDE4LjE1MzQgOC4wMTU0NSAxNy43OTc4IDguMDkxODcgMTcuMzMxNEw4LjY4Njk1IDEzLjcwMDFMNi4xNjU0NSAxMS4xMjk2QzUuODQxNyAxMC43OTk2IDYuMDE5OTMgMTAuMjI0MyA2LjQ2NzExIDEwLjE1NTlMOS45NTI0MiA5LjYyMjcyWiIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI%2BPC9wYXRoPjxwYXRoIGQ9Ik0yMiAxMkwyMyAxMiIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI%2BPC9wYXRoPjxwYXRoIGQ9Ik0xMiAyVjEiIHN0cm9rZT0iI2ZmZmZmZiIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD48cGF0aCBkPSJNMTIgMjNWMjIiIHN0cm9rZT0iI2ZmZmZmZiIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD48cGF0aCBkPSJNMjAgMjBMMTkgMTkiIHN0cm9rZT0iI2ZmZmZmZiIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD48cGF0aCBkPSJNMjAgNEwxOSA1IiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48L3BhdGg%2BPHBhdGggZD0iTTQgMjBMNSAxOSIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI%2BPC9wYXRoPjxwYXRoIGQ9Ik00IDRMNSA1IiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48L3BhdGg%2BPHBhdGggZD0iTTEgMTJMMiAxMiIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI%2BPC9wYXRoPjwvZz48ZGVmcz48Y2xpcFBhdGggaWQ9ImNsaXAwXzMwNTdfMTQ2MjgiPjxyZWN0IHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgZmlsbD0id2hpdGUiPjwvcmVjdD48L2NsaXBQYXRoPjwvZGVmcz48L3N2Zz4%3D&color=eeaf00">
    </a>
    <a href="https://github.com/NexaAI">
        <img alt="GitHub followers" src="https://img.shields.io/github/followers/bapo2?label=follow%20bapo2&style=flat-square&logo=github">
    </a>
<h4>