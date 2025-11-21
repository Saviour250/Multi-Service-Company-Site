import reflex as rx


class ShowcaseState(rx.State):
    selected_category: str = "All"
    is_lightbox_open: bool = False
    selected_image: dict[str, str] = {}
    categories: list[str] = [
        "All",
        "Construction",
        "Branding",
        "Painting",
        "Car Repair",
    ]
    items: list[dict[str, str]] = [
        {
            "id": "1",
            "title": "Victorian Home Restoration",
            "category": "Construction",
            "description": "Complete exterior renovation of a 19th-century Victorian home.",
            "before": "https://images.unsplash.com/photo-1504618223453-5c5085700b72?q=80&w=1000&auto=format&fit=crop",
            "after": "https://images.unsplash.com/photo-1600596542815-22b8c153bd95?q=80&w=1000&auto=format&fit=crop",
        },
        {
            "id": "2",
            "title": "Tech Startup Rebranding",
            "category": "Branding",
            "description": "Modernizing the visual identity for a fintech startup.",
            "before": "https://images.unsplash.com/photo-1626785774573-4b799312c95d?q=80&w=1000&auto=format&fit=crop",
            "after": "https://images.unsplash.com/photo-1626785774625-ddcddc3445e9?q=80&w=1000&auto=format&fit=crop",
        },
        {
            "id": "3",
            "title": "Luxury Apartment Interior",
            "category": "Painting",
            "description": "High-end interior painting and finishing.",
            "before": "https://images.unsplash.com/photo-1531835551805-16d864c8d311?q=80&w=1000&auto=format&fit=crop",
            "after": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?q=80&w=1000&auto=format&fit=crop",
        },
        {
            "id": "4",
            "title": "Classic Car Restoration",
            "category": "Car Repair",
            "description": "Bodywork and paint restoration for a vintage Mustang.",
            "before": "https://images.unsplash.com/photo-1619976769983-73d0932e865b?q=80&w=1000&auto=format&fit=crop",
            "after": "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?q=80&w=1000&auto=format&fit=crop",
        },
        {
            "id": "5",
            "title": "Modern Kitchen Remodel",
            "category": "Construction",
            "description": "Open concept kitchen renovation with island installation.",
            "before": "https://images.unsplash.com/photo-1484154218962-a1c002085d2f?q=80&w=1000&auto=format&fit=crop",
            "after": "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?q=80&w=1000&auto=format&fit=crop",
        },
        {
            "id": "6",
            "title": "Commercial Office Painting",
            "category": "Painting",
            "description": "Refreshing corporate office space with modern color palette.",
            "before": "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=1000&auto=format&fit=crop",
            "after": "https://images.unsplash.com/photo-1497366811353-6870744d04b2?q=80&w=1000&auto=format&fit=crop",
        },
    ]

    @rx.event
    def set_category(self, category: str):
        self.selected_category = category

    @rx.event
    def open_lightbox(self, item: dict[str, str]):
        self.selected_image = item
        self.is_lightbox_open = True

    @rx.event
    def close_lightbox(self):
        self.is_lightbox_open = False

    @rx.var
    def filtered_items(self) -> list[dict[str, str]]:
        if self.selected_category == "All":
            return self.items
        return [
            item for item in self.items if item["category"] == self.selected_category
        ]