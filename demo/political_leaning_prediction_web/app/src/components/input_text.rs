use dioxus::prelude::*;

#[component]
pub(crate) fn InputText() -> Element {
    rsx! {
        div {
            class: "flex-grow h-64 md:h-auto flex flex-col",
            label {
                class: "ps-4 font-semibold",
                r#for: "input_text",
                "Input text"
            }
            textarea {
                id: "input_text",
                name: "text",
                required: true,
                class: "p-4 flex-grow font-medium outline-none border shadow hover:shadow-md focus:shadow-lg rounded-xl resize-none transition-[box-shadow] duration-300",
            }
        }
    }
}
