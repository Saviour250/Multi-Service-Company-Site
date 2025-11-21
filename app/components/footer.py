import reflex as rx
from app.states.theme_state import ThemeState


def footer_link(text: str, href: str = "#") -> rx.Component:
    return rx.el.li(
        rx.el.a(
            text,
            href=href,
            class_name=rx.cond(
                ThemeState.is_dark,
                "text-slate-400 hover:text-orange-500 transition-colors",
                "text-slate-500 hover:text-orange-600 transition-colors",
            ),
        ),
        class_name="mb-3",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon("layers", class_name="h-8 w-8 text-orange-500"),
                        rx.el.span(
                            "VisionEdge",
                            class_name=rx.cond(
                                ThemeState.is_dark,
                                "ml-2 text-xl font-bold text-white",
                                "ml-2 text-xl font-bold text-slate-900",
                            ),
                        ),
                        class_name="flex items-center mb-6",
                    ),
                    rx.el.p(
                        "Your trusted partner for branding, construction, painting, and automotive excellence. Delivering vision with precision.",
                        class_name=rx.cond(
                            ThemeState.is_dark,
                            "text-slate-400 mb-6 pr-4",
                            "text-slate-500 mb-6 pr-4",
                        ),
                    ),
                    rx.el.div(
                        rx.el.a(
                            rx.icon("facebook", class_name="w-5 h-5"),
                            href="#",
                            class_name="text-slate-400 hover:text-orange-500 transition-colors",
                        ),
                        rx.el.a(
                            rx.icon("instagram", class_name="w-5 h-5"),
                            href="#",
                            class_name="text-slate-400 hover:text-orange-500 transition-colors",
                        ),
                        rx.el.a(
                            rx.icon("twitter", class_name="w-5 h-5"),
                            href="#",
                            class_name="text-slate-400 hover:text-orange-500 transition-colors",
                        ),
                        rx.el.a(
                            rx.icon("linkedin", class_name="w-5 h-5"),
                            href="#",
                            class_name="text-slate-400 hover:text-orange-500 transition-colors",
                        ),
                        class_name="flex space-x-4",
                    ),
                    class_name="col-span-1 md:col-span-2 lg:col-span-4",
                ),
                rx.el.div(
                    rx.el.h4(
                        "Services",
                        class_name=rx.cond(
                            ThemeState.is_dark,
                            "text-white font-bold mb-6",
                            "text-slate-900 font-bold mb-6",
                        ),
                    ),
                    rx.el.ul(
                        footer_link("Branding & Design"),
                        footer_link("Interior Painting"),
                        footer_link("Construction"),
                        footer_link("Car Repair"),
                        footer_link("Showcase", "/showcase"),
                        class_name="list-none",
                    ),
                    class_name="col-span-1 md:col-span-2 lg:col-span-2",
                ),
                rx.el.div(
                    rx.el.h4(
                        "Company",
                        class_name=rx.cond(
                            ThemeState.is_dark,
                            "text-white font-bold mb-6",
                            "text-slate-900 font-bold mb-6",
                        ),
                    ),
                    rx.el.ul(
                        footer_link("About Us"),
                        footer_link("Careers"),
                        footer_link("Privacy Policy"),
                        footer_link("Terms of Service"),
                        footer_link("Admin Login", "/admin"),
                        class_name="list-none",
                    ),
                    class_name="col-span-1 md:col-span-2 lg:col-span-2",
                ),
                rx.el.div(
                    rx.el.h4(
                        "Contact",
                        class_name=rx.cond(
                            ThemeState.is_dark,
                            "text-white font-bold mb-6",
                            "text-slate-900 font-bold mb-6",
                        ),
                    ),
                    rx.el.ul(
                        rx.el.li(
                            rx.el.div(
                                rx.icon(
                                    "map-pin",
                                    class_name="w-5 h-5 text-orange-500 mr-3 shrink-0",
                                ),
                                rx.el.span(
                                    "123 Business Ave, Tech City, TC 90210",
                                    class_name="text-sm",
                                ),
                                class_name="flex items-start",
                            ),
                            class_name=rx.cond(
                                ThemeState.is_dark,
                                "text-slate-400 mb-4",
                                "text-slate-500 mb-4",
                            ),
                        ),
                        rx.el.li(
                            rx.el.div(
                                rx.icon(
                                    "phone",
                                    class_name="w-5 h-5 text-orange-500 mr-3 shrink-0",
                                ),
                                rx.el.span("+1 (555) 123-4567", class_name="text-sm"),
                                class_name="flex items-center",
                            ),
                            class_name=rx.cond(
                                ThemeState.is_dark,
                                "text-slate-400 mb-4",
                                "text-slate-500 mb-4",
                            ),
                        ),
                        rx.el.li(
                            rx.el.div(
                                rx.icon(
                                    "mail",
                                    class_name="w-5 h-5 text-orange-500 mr-3 shrink-0",
                                ),
                                rx.el.span(
                                    "hello@visionedge.com", class_name="text-sm"
                                ),
                                class_name="flex items-center",
                            ),
                            class_name=rx.cond(
                                ThemeState.is_dark,
                                "text-slate-400 mb-4",
                                "text-slate-500 mb-4",
                            ),
                        ),
                        class_name="list-none",
                    ),
                    class_name="col-span-1 md:col-span-2 lg:col-span-4",
                ),
                class_name="grid grid-cols-1 md:grid-cols-6 lg:grid-cols-12 gap-12",
            ),
            rx.el.div(
                rx.el.p(
                    "© 2024 VisionEdge Group Ltd. All rights reserved.",
                    class_name=rx.cond(
                        ThemeState.is_dark,
                        "text-center text-slate-500 text-sm",
                        "text-center text-slate-400 text-sm",
                    ),
                ),
                class_name=rx.cond(
                    ThemeState.is_dark,
                    "mt-16 pt-8 border-t border-slate-800",
                    "mt-16 pt-8 border-t border-gray-100",
                ),
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
        ),
        class_name=rx.cond(
            ThemeState.is_dark,
            "bg-slate-900 pt-20 pb-10 border-t border-slate-800",
            "bg-white pt-20 pb-10 border-t border-gray-100",
        ),
    )