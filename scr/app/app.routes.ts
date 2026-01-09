import { Routes } from '@angular/router';

export const routes: Routes = [
  // ✅ Default redirect
  {
    path: '',
    redirectTo: 'home',
    pathMatch: 'full',
  },

  // ✅ Home
  {
    path: 'home',
    loadComponent: () =>
      import('./home/home.page').then((m) => m.HomePage),
  },

  // ✅ Folder
  {
    path: 'folder/:id',
    loadComponent: () =>
      import('./folder/folder.page').then((m) => m.FolderPage),
  },

  // ✅ School Pages
  {
    path: 'the-school',
    loadComponent: () =>
      import('./pages/the-school/the-school.page').then((m) => m.TheSchoolPage),
  },
  {
    path: 'administration',
    loadComponent: () =>
      import('./pages/administration/administration.page').then((m) => m.AdministrationPage),
  },
  {
    path: 'academics',
    loadComponent: () =>
      import('./pages/academics/academics.page').then((m) => m.AcademicsPage),
  },
  {
    path: 'faculty',
    loadComponent: () =>
      import('./pages/faculty/faculty.page').then((m) => m.FacultyPage),
  },
  {
    path: 'students',
    loadComponent: () =>
      import('./pages/students/students.page').then((m) => m.StudentsPage),
  },

  // ✅ RIE Main Page & Subpages
  {
    path: 'rie',
    loadComponent: () =>
      import('./pages/rie/rie.page').then((m) => m.RiePage),
  },
  {
    path: 'rie/journal',
    loadComponent: () =>
      import('./pages/rie/journal/journal.page').then((m) => m.JournalPage),
  },
  {
    path: 'rie/research',
    loadComponent: () =>
      import('./pages/rie/research/research.page').then((m) => m.ResearchPage),
  },
  {
    path: 'rie/manual',
    loadComponent: () =>
      import('./pages/rie/manual/manual.page').then((m) => m.ManualPage),
  },
  {
    path: 'rie/milestone',
    loadComponent: () =>
      import('./pages/rie/milestone/milestone.page').then((m) => m.MilestonePage),
  },
  {
    path: 'rie/cmd',
    loadComponent: () =>
      import('./pages/rie/cmd/cmd.page').then((m) => m.CmdPage),
  },
  {
    path: 'rie/extension',
    loadComponent: () =>
      import('./pages/rie/extension/extension.page').then((m) => m.ExtensionPage),
  },

  // ✅ Library
  {
    path: 'library',
    loadComponent: () =>
      import('./pages/library/library.page').then((m) => m.LibraryPage),
  },

  // ✅ Alumni Pages
  {
    path: 'alumni',
    loadComponent: () =>
      import('./pages/alumni/alumni.page').then((m) => m.AlumniPage),
  },
  {
    path: 'alumni/association',
    loadComponent: () =>
      import('./pages/alumni/association/association.page').then((m) => m.AssociationPage),
  },
  {
    path: 'alumni/events',
    loadComponent: () =>
      import('./pages/alumni/events/events.page').then((m) => m.EventsPage),
  },
  {
    path: 'alumni/directory',
    loadComponent: () =>
      import('./pages/alumni/directory/directory.page').then((m) => m.DirectoryPage),
  },

  // ✅ Campuses Pages
  {
    path: 'campuses',
    loadComponent: () =>
      import('./pages/campuses/campuses.page').then((m) => m.CampusesPage),
  },
  {
    path: 'campuses/delcarmen',
    loadComponent: () =>
      import('./pages/campuses/delcarmen/delcarmen.page').then((m) => m.DelcarmenPage),
  },
  {
    path: 'campuses/mainit',
    loadComponent: () =>
      import('./pages/campuses/mainit/mainit.page').then((m) => m.MainitPage),
  },
  {
    path: 'campuses/malimono',
    loadComponent: () =>
      import('./pages/campuses/malimono/malimono.page').then((m) => m.MalimonoPage),
  },
];
