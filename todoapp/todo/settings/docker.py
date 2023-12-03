if IN_DOCKER: # type: ignore
    print("running")
    assert MIDDLEWARE[:-1] == [ # type: ignore
        "django.middleware.security.SecurityMiddleware"   
    ]