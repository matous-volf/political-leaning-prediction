use crate::route::Route;
use dioxus::prelude::*;

const FAVICON: Asset = asset!("/assets/images/favicon.ico");
const TAILWIND_CSS: Asset = asset!("/assets/styles/tailwind_output.css");
const CUSTOM_CSS: Asset = asset!("/assets/styles/custom.css");
const FONTS_URL: &str = "https://use.typekit.net/ycd3xdz.css";

#[component]
pub(crate) fn App() -> Element {
    rsx! {
        document::Link { rel: "icon", href: FAVICON }
        document::Stylesheet { href: TAILWIND_CSS }
        document::Stylesheet { href: CUSTOM_CSS }
        document::Stylesheet { href: FONTS_URL }

        div {
            class: "min-h-screen p-8 flex flex-col text-xl text-slate-600",
            Router::<Route> {}
        }
    }
}
