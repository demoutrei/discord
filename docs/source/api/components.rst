Component Reference
===================


This document serves as a comprehensive reference for all available components. It covers three main categories:

- **Layout Components**: For organizing and structuring content (Action Rows, Sections, Containers)
- **Content Components**: For displaying static text, images, and files (Text Display, Media Gallery, Thumbnails)
- **Interactive Components**: For user interactions (Buttons, Select Menus, Text Input)


To use these components, you need to send the :attr:`~discord.flags.MessageFlags.IS_COMPONENTS_V2` which can be sent on a per-message basis. Once a message has been sent with this flag, it can't be removed from that message. This enables the new components system with the following changes:

- The :attr:`~discord.objects.Message.content` and :attr:`~discord.objects.Message.embeds` fields will no longer work but you'll be able to use :class:`~discord.components.TextDisplay` and :class:`~discord.components.Container` as replacements.
- Attachments won't show by default--they must be exposed through components.
- The :attr:`~discord.objects.Message.poll` and :attr:`~discord.objects.Message.stickers` fields are disabled.
- Messages allow up to 40 total components.


**Components**

Components allow you to style and structure your messages, modals, and interactions. They are interactive elements that can create rich user experiences in your Discord applications.


**Anatomy of a Component**

All components have the following fields:

.. autoattribute:: discord.components._base.Component.id

.. autoattribute:: discord.components._base.Component.type

The ``id`` field is optional and is used to identify components in the response from an interaction. The ``id`` must be unique within the message and is generated sequentially if left empty. Sending components with an ``id`` of ``0`` is allowed but will be treated as empty and replaced by the API.

Additionally, interactive components like buttons and selects must have a ``custom_id`` field. The developer defines this field when sending the component payload, and it is returned in the interaction payload sent when a user interactions with the component. ``custom_id`` is only available on interactive components and must be unique per component. Multiple components on the same message must not share the same ``custom_id``

.. autoattribute:: discord.components._base.InteractiveComponent.custom_id


Checkbox and Checkbox Group
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: discord.components.CheckboxComponent()

.. autoclass:: discord.components.CheckboxGroupComponent()

.. autoclass:: discord.components.CheckboxGroupOption()


Container
^^^^^^^^^

.. autoclass:: discord.components.ContainerComponent()

.. admonition:: Container Child Components
    :collapsible:

    :class:`~discord.components.ActionRowComponent`
    :class:`~discord.components.TextDisplayComponent`
    :class:`~discord.components.SectionComponent`
    :class:`~discord.components.MediaGalleryComponent`
    :class:`~discord.components.SeparatorComponent`
    :class:`~discord.components.FileComponent`


File Upload
^^^^^^^^^^^

.. autoclass:: discord.components.FileUploadComponent()


Label
^^^^^

.. autoclass:: discord.components.LabelComponent()

.. admonition:: Label Child Components
    :collapsible:

    :class:`~discord.components.TextInputComponent`
    :class:`~discord.components.StringSelectComponent`
    :class:`~discord.components.UserSelectComponent`
    :class:`~discord.components.RoleSelectComponent`
    :class:`~discord.components.MentionableSelectComponent`
    :class:`~discord.components.ChannelSelectComponent`
    :class:`~discord.components.FileUploadComponent`
    :class:`~discord.components.RadioGroupComponent`
    :class:`~discord.components.CheckboxGroupComponent`
    :class:`~discord.components.CheckboxComponent`


Radio Group
^^^^^^^^^^^

.. autoclass:: discord.components.RadioGroupComponent()

.. autoclass:: discord.components.RadioGroupOption()